from github import GitHub
import json
import github.db.repositories.LanguagesAggregate

username = "github_username"
db_path_account = "C:/GitHub.Accounts.sqlite3"
db_path_api = "C:/GitHub.Apis.sqlite3"
db_path_repo = "C:/GitHub.Repositories.{0}.sqlite3".format(username)

repo_name = "GitHub.Repo.Create.201701281344"
repo_description = "GitHubリモートリポジトリを生成しローカルDBに挿入する"
repo_homepage = ""

g = GitHub.GitHub(db_path_account, db_path_api, db_path_repo, username)
res = g.db.upload(repo_name, repo_description, repo_homepage)
#res = g.db.update_local_db()

aggr = github.db.repositories.LanguagesAggregate.LanguagesAggregate(db_path_repo)
aggr.show()
