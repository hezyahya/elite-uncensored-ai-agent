from e2b import Sandbox
import asyncio

async def run_command(cmd):
    async with Sandbox.create() as sandbox:
        result = await sandbox.commands.run(cmd)
        return result.stdout

# Example usage
if __name__ == "__main__":
    print(asyncio.run(run_command("ls -la")))