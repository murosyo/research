from getdata import get_data_by_tag
from getdata import get_source_code

def main():
    # 使用例
    # tag = 'greedy'  # 取得したいタグを入力してください
    # tag = 'dp'
    tag = 'brute+force'
    merge_list = get_data_by_tag(tag)
    source_code_list = get_source_code(merge_list)

if __name__ == '__main__':
    main()