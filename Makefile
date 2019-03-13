VERSION ?= $(if $(TRAVIS_TAG),$(TRAVIS_TAG),$(if $(TAG_NAME),$(TAG_NAME),dev))
OPENAPIGEN_IMAGE ?= openapitools/openapi-generator-cli:v3.3.4

deploy_pypi:
ifdef VERSION
	rm -rf dist

	cd api && python setup.py sdist bdist_wheel

	twine upload -u ${PYPI_USER} -p ${PYPI_PASSWORD} api/dist/*
else
	@echo "not tagged"
endif

clean:
	rm -rf api
	rm openapi.yaml

api: openapi.yaml
	docker run --rm --user `id -u`:`id -g` -v ${PWD}:/local ${OPENAPIGEN_IMAGE} \
	           generate -i /local/openapi.yaml \
	           --git-user-id rienafairefr \
	           --git-repo-id ynab \
	           -g python -o /local/api -DprojectName=pyynab -DpackageName=ynab \
	           -DpackageVersion="$(VERSION)" -DappDescription="pyynab, an autogenerated package to access public API of app.youneedabudget.com"\
	           -DappName="ynab" -DinfoEmail="rienafairefr@gmail.com"

openapi.yaml:
	docker run --rm --user `id -u`:`id -g` -v ${PWD}:/local ${OPENAPIGEN_IMAGE} \
	           generate -i /local/swagger.json \
	           -g openapi-yaml -o /local/openapi-yaml
	cp openapi-yaml/openapi/openapi.yaml .
	rm -rf openapi-yaml
	python patch_openapi.py
