#!/usr/bin/python
from ansible.module_utils.basic import *
from subprocess import check_output


def main():
    module = AnsibleModule(argument_spec={})

    cmd = "ps -ef | grep tomcat"
    ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    x = ps.communicate()[0]

    module.exit_json(changed=False, msg=x)


if __name__ == '__main__':
    main()
