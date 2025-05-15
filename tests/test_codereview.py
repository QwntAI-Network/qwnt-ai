from src.agents.codereview import CodeReviewAgent
import os

def test_codereview_flags_issues():
    test_file = "test_script.py"
    with open(test_file, "w") as f:
        f.write("print('This is a test')\\n" + "a = 'x' * 120\\n")
    agent = CodeReviewAgent(name="QA")
    result = agent.run(test_file)
    assert "Line 1 uses print()" in result
    assert "Line 2 too long" in result
