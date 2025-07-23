from app.ai_agent import check_guidelines

def test_check_guidelines():
    text = "This are wrong sentence."
    results = check_guidelines(text)
    assert len(results) > 0
