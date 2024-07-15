import typer
from typing import Optional

from di_container import container
from chains.code_chain import execute_code_chain
from configuration.settings import load_config
from llm.llm_providers import register_llm_provider

app = typer.Typer()

def setup_di():
    config = load_config()
    register_llm_provider(container, config)
    
@app.command()
def code_gen(
    task: str = typer.Option(..., prompt="What should the code do?", help="Define the task to be performed"),
    language: str = typer.Option("python", prompt="Which programming language?", help="Specify the programming language"),
):
    """
    Generate code based on provided task and language
    """
    llm = container.get('llm')
    
    result = execute_code_chain(llm=llm, language=language, task=task)
    
    typer.echo(f"\nGenerated {language} code for the task: '{task}'\n")
    typer.echo(result)
    
    save = typer.confirm("Do you want to save this code to a file?")
    if save:
        filename = typer.prompt("Enter filepath/filename to save the code")
        with open(filename, "w") as f:
            f.write(result)
        typer.echo(f"Code saved to {filename}")

if __name__ == "__main__":
    setup_di()
    app()