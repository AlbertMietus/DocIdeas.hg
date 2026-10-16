# Copyright (C) ALbert Mietus, SoftwareBeterMaken.nl; 2017. Part of MESS-DocIdeas
default: html

docs_TARGETS =	html
docs: 		${docs_TARGETS}
all: 		docs

DOCd          =  .
OUTd          =  __result/
TMPd	     ?=  tmp/
SPHINX_CACHE  =  ${TMPd}sphinx_cache


##
## User-friendly check for sphinx-build
##
SPHINXBUILD   = sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
  $(error The '$(SPHINXBUILD)' command was not found. Make sure you selected a "Python3" (virt)env with Sphinx installed)
endif

##
## Pass make option to sphinx-build
##
ifneq (,$(findstring B,$(MAKEFLAGS)))
  build_opts+=-a -E
endif
ifneq (,$(findstring J,$(MAKEFLAGS)))
  build_opts+=-j
endif


SPHINX_OPTS = ${build_opts} -d ${SPHINX_CACHE}

${docs_TARGETS}:
	${PYTHONPATH} $(SPHINXBUILD) -q -c . -b $@ ${SPHINX_OPTS}  ${DOCd} ${OUTd}$@
	@echo "Build finished, See: ${OUTd}$@"

clean:
	rm -rf ${SPHINX_CACHE}

cleaner veryclean: clean
	rm -rf ${OUTd}*

cleanest: cleaner; #nothing extra

_sync-bookmarks:
	for b in $$(hg branches | awk '{print $$1}'); do \
	    hg bookmark -f -r "$$b" "_g_$$b"; \
	done

push-all: _sync-bookmarks
	-hg push
	-hg push --all SF
	-hg push --all github

RTD RTfD RTFD: push-all


wc:
	@echo "lines	words	file"
	@wc -lw `find -L CCastle/ -iname \*rst`|sort -r | grep -v /index.rst | grep -v /zz.todo.rst

sidebar:
	@grep "include::" `find CCastle/ -type f -name \*.rst` /dev/null | grep sidebar| sort| sed 's/:../:\t\t ../'
