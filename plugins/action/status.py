from xmltodict import parse as parse_xml

from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        super(ActionModule, self).run(tmp, task_vars)
        result = self._execute_module(
            module_name='ansibleguy.linuxha.status',
            module_args=self._task.args,
            task_vars=task_vars,
            tmp=tmp
        )

        if '_action' in result:
            # if 'detailed: true'
            result['data'] = parse_xml(
                result['_action'],
                attr_prefix=''
            )['crm_mon']
            result.pop('_action')

        return result
