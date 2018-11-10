#!/usr/bin/env python

import sys
import os
import re
import shutil
import helix.settings
import helix.logs

log = helix.logs.get_logger()

def find_runner(search_dir, framework):
    for root, dirs, files in os.walk(search_dir):
        for file_name in files:
            if re.search(framework.replace(r".", r"\.") + r"[\\/]xunit\.console\.(dll|exe)$", os.path.join(root, file_name)):
                return os.path.join(root, file_name)

def main():
    settings = helix.settings.settings_from_env()

    if (sys.argv.count < 2):
        log.error("No target framework was passed to xunit-runner-setup.py")
        return 1

    workitem_dir = settings.workitem_payload_dir
    correlation_dir = settings.correlation_payload_dir
    target_framework = sys.argv[1]

    runner_dll_loc = correlation_dir + "/"

    shutil.copy2()
    
    return 0

if __name__ == 'main':
    sys.exit(main())
