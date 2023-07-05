import requests
from bs4 import BeautifulSoup
import json
import collections

def get_data_by_tag(tag):
    url = 'https://codeforces.com/api/problemset.problems?tags=' + tag
    # url = "https://codeforces.com/api/problemset.problems?tags=dp"
    # url = "https://codeforces.com/api/problemset.problems?tags=brute_force"

    # APIからデータを取得
    response = requests.get(url)
    data = response.json()

    # 問題名のリスト
    problem_name_list = []
    # コンテストIDのリスト
    contest_id_list = []
    # 問題の難易度のリスト
    problem_difficulty_list = []
    # 問題に付与されているタグのリスト
    problem_tag_list = []
    # 問題のレート（レベル感）のリスト
    problem_rate_list = []
    # 問題を解くことで付与されるポイントのリスト
    problem_point_list = []
    # 上記で集めたものをマージするリスト
    merge_list = []

    # 問題のリストを取得
    problems = data['result']['problems']

    # 'greedy'タグの問題のみを抽出
    greedy_problems = [problem for problem in problems if len(problem['tags']) == 1]

    # 結果を表示
    for problem in greedy_problems:
        # problem_name_list.append(problem['name'])
        contest_id_list.append(problem['contestId'])
        problem_difficulty_list.append(problem['index'])
        # problem_tag_list.append("".join(problem['tags']))
        # problem_rate_list.append(problem['rating'])
        # problem_point_list.append(problem['points'])
        # merge_list.append([problem['index'], problem['contestId']])
        # merge_list.append([problem['contestId'], problem['index'], problem['name'], "".join(problem['tags'])])
        # merge_list.append(problem['contestId'], problem['index'], problem['name'], problem['points'], problem['rating'], problem['tags'])
    for i,j in zip(contest_id_list,problem_difficulty_list):
        merge_list.append([i,j])
    # print(merge_list)
    # print(problem_tag_list)
    return merge_list
    # return contest_id_list

def get_source_code(merge_list):
    # print(merge_list)
    contest_id = []
    difficulty = []
    for i in range(len(merge_list)):
        # print(merge_list[i][0])
        # print(merge_list[i][1])
        difficulty.append(merge_list[i][1])
        contest_id.append(merge_list[i][0])

    # print(difficulty)
    # print(contest_id)

    output_list = []
    note_list = []
    problem_statement_list = []

    for i in range(len(contest_id)):
        # url = "https://codeforces.com/contest/{contest_id}/submission/211291886"
        url = "https://codeforces.com/contest/" + str(contest_id[i]) + "/problem/" + str(difficulty[i])
        # url = "https://codeforces.com/contest/" + str(contest_id[i]) + "/status"
        # print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # コードの取得（現状一つしか取れない）
        # print(soup.find('pre').text)
        # 問題文を取得
        problem_statement_list.append(soup.div.find(class_='tex-font-style-it', recursive=False))
        # 問題のタイトルを取得
        # print(soup.find('div', class_='title').text)

        # 問題の入力例を取得
        # 問題の出力例を取得       
        # output_list.append(soup.find('div', class_='output').text[6:])
        # note_list.append(soup.find('div', class_='note').text)
    print(problem_statement_list)
    # print(output_list)
    # print(note_list)
        # output_list.pop('Output')
        # 問題のNoteを取得


    # submissions = soup.select('.status-frame-datatable .status-small')
    # for submission in submissions:
    #     source_code = submission.find('pre').text
        # print(source_code)