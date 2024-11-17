import os
def get_project_path():
    project_name ="auto_test"
    file_path=os.path.dirname(__file__)
    return file_path[:file_path.find(project_name)+len(project_name)]

def sep(path,add_sep_before=False, add_sep_after=False):
    all_path=os.sep.join(path)
    if add_sep_before:
        all_path=os.sep+all_path
    if add_sep_after:
        all_path=all_path+os.sep
    return all_path

if __name__ == '__main__':
  print(sep(["config", "environment.yaml"], True))
