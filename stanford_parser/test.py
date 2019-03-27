from parser import Parser
stanford_parser = Parser()
dependencies = stanford_parser.parseToStanfordDependencies("The girl I met was your sister.")
print dependencies
tupleResult = [(rel, gov.text, dep.text) for rel, gov, dep in dependencies.dependencies]
print tupleResult