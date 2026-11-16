.PHONY: check dist install-claude-code

check dist:
	python3 scripts/build.py --check

install-claude-code:
	python3 scripts/install_claude_code.py
