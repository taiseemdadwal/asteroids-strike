VENV = .venv
BIN =  ${VENV}/bin


.PHONY: dev
dev: requirements.txt
	python3 -m venv ${VENV}
	. .venv/bin/activate
	./${BIN}/pip install -r requirements.txt

.PHONY: run
run:
	python src/__main__.py
venv:
	chmod +x ./${BIN}/activate
	source ./${BIN}/activate

clean:
	rm -rf ${VENV}
	rm -rf venv
