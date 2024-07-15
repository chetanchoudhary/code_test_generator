import typer

from chains.code_chain import execute_code_chain

app = typer.Typer()

DEFAULT_LANGUAGE = "python"
DEFAULT_TASK = "return list of numbers"

@app.command()
def code_gen(task: str = DEFAULT_TASK, language: str = DEFAULT_LANGUAGE):
    """
    Generate code based on provided task and language
    
    :param task: Define task that needs to be performed.
    :param language: Programming Language (default is "python")
    """
    result = execute_code_chain(language=language, task=task)
    print(result)
    return result


if __name__ == "__main__":
    app()