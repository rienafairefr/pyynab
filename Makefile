VERSION ?= $(shell pipenv run python -c "from setuptools_scm import get_version;print(get_version())")
OPENAPIGEN_IMAGE ?= openapitools/openapi-generator-cli:v4.1.0

clean:
	rm -rf api
	rm openapi.yaml

api: openapi.yaml
	docker run --rm --user `id -u`:`id -g` -v ${PWD}:/local ${OPENAPIGEN_IMAGE} \
	           generate -i /local/openapi.yaml \
	           --git-user-id rienafairefr \
	           --git-repo-id ynab \
	           -g python -o /local/api \
	           --additional-properties projectName=pyynab --package-name ynab \
	           --additional-properties packageVersion="$(VERSION)" \
	           --additional-properties appDescription="pyynab, an autogenerated package to access public API of app.youneedabudget.com" \
	           --additional-properties appName="ynab" \
	           --additional-properties infoEmail="rienafairefr@gmail.com"

openapi.yaml:
	docker run --rm --user `id -u`:`id -g` -v ${PWD}:/local ${OPENAPIGEN_IMAGE} \
	           generate -i /local/swagger.json \
	           -g openapi-yaml -o /local/openapi-yaml
	cp openapi-yaml/openapi/openapi.yaml .
	rm -rf openapi-yaml
	pipenv run python patch_openapi.py
