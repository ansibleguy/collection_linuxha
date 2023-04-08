from xmltodict import parse as parse_xml

from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        super().run(tmp, task_vars)
        result = self._execute_module(
            module_name='ansibleguy.linuxha.status',
            module_args=self._task.args,
            task_vars=task_vars,
            tmp=tmp
        )

        if '_data' in result:
            # if 'detailed: true'
            result['data'] = parse_xml(
                result['_data'],
                attr_prefix=''
            )['crm_mon']
            result.pop('_data')

        return result
