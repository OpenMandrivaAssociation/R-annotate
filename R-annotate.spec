%bcond_with internet
%bcond_with bootstrap
%global packname  annotate
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.32.1
Release:          3
Summary:          Annotation for microarrays
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-AnnotationDbi 
Requires:         R-Biobase R-AnnotationDbi R-DBI R-xtable R-graphics
Requires:         R-utils R-stats R-methods R-Biobase R-tkWidgets R-XML
%if %{without bootstrap}
Requires:         R-hgu95av2.db R-genefilter R-Biostrings R-rae230a.db
Requires:         R-rae230aprobe R-GO.db R-org.Hs.eg.db R-org.Mm.eg.db
Requires:         R-hom.Hs.inp.db
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-AnnotationDbi
BuildRequires:    R-Biobase R-AnnotationDbi R-DBI R-xtable R-graphics R-utils
BuildRequires:    R-stats R-methods  R-Biobase R-tkWidgets R-XML
%if %{without bootstrap}
BuildRequires:    R-hgu95av2.db R-genefilter R-Biostrings R-rae230a.db
BuildRequires:    R-rae230aprobe R-GO.db R-org.Hs.eg.db R-org.Mm.eg.db
BuildRequires:    R-hom.Hs.inp.db
%endif

%description
Using R enviroments for annotation.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
    %if %{with internet}
%check
%{_bindir}/R CMD check %{packname}
    %endif
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/misc
