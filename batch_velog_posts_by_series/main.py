import os

from batch_velog_posts_by_series import velog_config
from batch_velog_posts_by_series.get_all_posts_by_username import get_all_posts
from batch_velog_posts_by_series.get_series_by_username import send_graphql_query
from batch_velog_posts_by_series.replace_special_characters import replace_special_characters

# TODO os 환경변수로 이름 받기
name = "cksgodl"
# TODO runner 로컬 위치
repo_path = "C:\\Users\\cksgo\\Desktop\\velog_migration_scripts"

series_list = send_graphql_query(query=velog_config.get_series_query, name=name)
all_posts = get_all_posts(name)

filtered_posts = []

for series in series_list:
    filtered_posts = []

    # 시리즈 필터링
    for post in all_posts:
        post_series = post.get('series')
        if post_series and post_series.get('id') == series['id']:
            filtered_posts.append(post)

    # 폴더 만들기
    posts_dir = os.path.join(repo_path, series['name'])
    if not os.path.exists(posts_dir):
        os.makedirs(posts_dir)

    # 파일 쓰기
    for post in filtered_posts:
        file_name = replace_special_characters(post['title']) + '.md'
        file_path = os.path.join(posts_dir, file_name)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(post['body'])

    print("--------------")

