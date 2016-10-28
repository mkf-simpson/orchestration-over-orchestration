#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
            argument_spec = dict(
                image = dict(type='str'),
                volumes = dict(type='list'),
                links = dict(type='list'),
                ports = dict(type='list'),
                labels = dict(type='list'),
                cpu = dict(type='int'),
                memory = dict(type='int')
            )
    )
    module.exit_json(changed=True, something_else=module.params)

if __name__ == '__main__':
    main()

