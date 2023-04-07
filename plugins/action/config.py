from xmltodict import parse as parse_xml
from xml.parsers.expat import ExpatError

from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        super().run(tmp, task_vars)
        result = self._execute_module(
            module_name='ansibleguy.linuxha.config',
            module_args=self._task.args,
            task_vars=task_vars,
            tmp=tmp
        )

        if '_action' in result:
            # if 'detailed: true'
            try:
                result['data'] = parse_xml(
                    result['_action'],
                    attr_prefix=''
                )['cib']

            except ExpatError as e:
                result['rc'] = 1
                result['error'] = str(e)

            result.pop('_action')

        return result
