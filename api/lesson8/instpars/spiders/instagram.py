import scrapy
from scrapy.http import HtmlResponse
import re
import json
from urllib.parse import urlencode
from copy import deepcopy
from instpars.items import InstparsItem

class InstagramSpider(scrapy.Spider):
    name = 'instagram'
    allowed_domains = ['instagram.com']
    start_urls = ['https://instagram.com/']
    insta_login = 'aflyck'
    insta_pass = ''
    insta_login_link = 'https://www.instagram.com/accounts/login/ajax/'
    parse_users = ['mongodb', 'pikabu']
    list_follow = ['edge_followed_by', 'edge_follow']
    list_hash = ['c76146de99bb02f6415203be841dd25a', 'd04b0a864b4b54837c0d870b0e77e076']
    graphql_url = 'https://www.instagram.com/graphql/query/?'

    def parse(self, response:HtmlResponse):
        yield scrapy.FormRequest(
            self.insta_login_link,
            method='POST',
            callback=self.user_parse,
            formdata={'username':self.insta_login, 'enc_password':self.insta_pass},
            headers={'X-CSRFToken':self.fetch_csrf_token(response.text)}
        )

    def user_parse(self, response:HtmlResponse):
        ans = json.loads(response.text)
        if ans["authenticated"]:
            for parse_user in self.parse_users:
                yield response.follow(f'/{parse_user}',
                                      callback=self.data_parse,
                                      cb_kwargs={'username': parse_user}
            )

    def data_parse(self, response:HtmlResponse, username):
        user_id = self.fetch_user_id(response.text, username)
        variables = {"id": user_id,
                     "include_reel": True,
                     "fetch_mutual": True,
                     "first": 50
                     }
        for pos, post_hash in enumerate(self.list_hash):
            url = f'{self.graphql_url}query_hash={post_hash}&{urlencode(variables)}'
            yield response.follow(
                url,
                callback=self.follow_parse,
                cb_kwargs={'username': username,
                           'user_id': user_id,
                           'variables': deepcopy(variables),
                           'pos': deepcopy(pos),
                           'post_hash': post_hash}

            )

    def follow_parse(self, response:HtmlResponse, username, user_id, variables, pos, post_hash):
        j_data = json.loads(response.text)
        page_info = j_data.get('data').get('user').get(self.list_follow[pos]).get('page_info')
        if page_info.get('has_next_page'):
            variables['after'] = page_info.get('end_cursor')
            url = f'{self.graphql_url}query_hash={post_hash}&{urlencode(variables)}'
            yield response.follow(
                url,
                callback=self.follow_parse,
                cb_kwargs={'username': username,
                           'user_id': user_id,
                           'variables': deepcopy(variables),
                           'pos': deepcopy(pos),
                           'post_hash': post_hash})
        follows = j_data.get('data').get('user').get(self.list_follow[pos]).get('edges')
        for follow in follows:
            item = InstparsItem(
                source_id=user_id,
                source=username,
                user_id=follow['node']['id'],
                user_name=follow['node']['username'],
                photo=follow['node']['profile_pic_url'],
                follow=pos
            )
            yield item


    def fetch_csrf_token(self, text):
        match = re.search('\"csrf_token\":\"\\w+\"', text).group()
        return match.split(':').pop().replace(r'"','')

    def fetch_user_id(self, text, username):
        matched = re.search(
            '{\"id\":\"\\d+\",\"username\":\"%s\"}' % username, text
        ).group()
        return json.loads(matched).get('id')