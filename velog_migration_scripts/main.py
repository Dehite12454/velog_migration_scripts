import requests

from velog_migration_scripts import velog_config
from velog_migration_scripts.get_all_posts_by_username import get_all_posts
from velog_migration_scripts.get_series_by_username import send_graphql_query

# TODO os 환경변수로 이름 받기
name = "cksgodl"

series_list = send_graphql_query(query=velog_config.get_series_query, name=name)

# print(series_list)

all_posts = get_all_posts(name)

for series in series_list:
    filtered_posts = []
    for post in all_posts:
        post_series = post.get('series')
        if post_series and post_series.get('id') == series['id']:
            filtered_posts.append(post)

    print(series['name'])

    for post in filtered_posts:
        print(post['title'])
        print(post['body'])
        body = post['body'].replace("\n", "<br>")
        print(body)
    print("--------------")
