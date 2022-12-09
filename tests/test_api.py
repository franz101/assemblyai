from tube2blog.api import AssemblyAiAPI
import os

def test_assembly_ai():
    a = AssemblyAiAPI(os.environ["ASSEMBLYAI_API_KEY"])
    