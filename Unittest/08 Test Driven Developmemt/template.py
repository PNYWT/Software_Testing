import re

class Template:

    def __init__(self, template) -> None:
        self.template = template
        self.variables = {} #emptry dictionary

    def set(self, variable, value):
        self.variables[variable] = value

    def evaluate(self):
        result = self.replace_variables()
        self.check_for_messing_values(result)
        return result
    
    def replace_variables(self):
        result_Template = self.template
        for variable, value in self.variables.items():
            regex = "${" + variable +"}"
            result_Template = result_Template.replace(regex, value)
        return result_Template
    
    def check_for_messing_values(self, result):
        if re.match(".*\${.+}.*", result):
            print("AttributeError() ->",result)
            raise AttributeError()
        # reg = re.compile(".*\${.+}.*")
        # m = reg.match(result)
        # if m:
        #     raise AttributeError("No value for " + m.group())