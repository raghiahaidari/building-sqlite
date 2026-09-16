from enum import Enum

class MetaCommandResult(Enum):
    META_COMMAND_SUCCESS = "success"
    META_COMMAND_UNRECOGNIZED_COMMAND = "unrecognized"

class PrepareResult(Enum):
    PREPARE_SUCCESS = "success"
    PREPARE_UNRECOGNIZED_STATEMENT = "unrecognized"

class StatementType(Enum):
    STATEMENT_INSERT = "insert"
    STATEMENT_SELECT = "select"

class Statement:
    def __init__(self, statement_type: StatementType):
        self.type = statement_type

# Simple SQL compiler that recognizes "insert" and "select" statements
def do_meta_command(user_input: str) -> MetaCommandResult:
    if user_input == ".exit":
        return MetaCommandResult.META_COMMAND_SUCCESS
    else:
        return MetaCommandResult.META_COMMAND_UNRECOGNIZED_COMMAND

def prepare_statement(user_input: str) -> PrepareResult:
    if user_input.startswith("insert"):
        return PrepareResult.PREPARE_SUCCESS
    elif user_input.startswith("select"):
        return PrepareResult.PREPARE_SUCCESS
    else:
        return PrepareResult.PREPARE_UNRECOGNIZED_STATEMENT

# Simple virtual machine to execute "insert" and "select" statements
def execute_statement(statement: Statement):
    if statement.type == StatementType.STATEMENT_INSERT:
        return "This is where we would do an insert."
    elif statement.type == StatementType.STATEMENT_SELECT:
        return "This is where we would do a select."

def main():
    while True:
        print("db > ", end="")
        user_input = input().strip()
        if user_input.startswith("."):
            meta_command_result = do_meta_command(user_input)
            if meta_command_result == MetaCommandResult.META_COMMAND_SUCCESS:
                break
            else:
                print("Unrecognized command", user_input, ".\n")
        else:
            prepare_result = prepare_statement(user_input)
            if prepare_result == PrepareResult.PREPARE_SUCCESS:
                if user_input.startswith("insert"):
                    statement_type = StatementType.STATEMENT_INSERT
                elif user_input.startswith("select"):
                    statement_type = StatementType.STATEMENT_SELECT
                else:
                    print("Unrecognized statement type.\n")
                    continue

                stmt = Statement(statement_type)
                result = execute_statement(stmt)
                print(result + "\n")
            else:
                print("Unrecognized keyword at start of", user_input, ".\n")
if __name__ == "__main__":
    main()