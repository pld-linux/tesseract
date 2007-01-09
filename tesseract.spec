Summary:	Tesseract Open Source OCR Engine.
Name:		tesseract
Version:	1.02
Release:	1
License:	Apache Software License v2
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/tesseract-ocr/%{name}-%{version}.tar.gz
# Source0-md5:	473389c9f447b081ac199ba3a0e55b27
URL:		http://sourceforge.net/projects/tesseract-ocr
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A commercial quality OCR engine originally developed at HP between
1985 and 1995. In 1995, this engine was among the top 3 evaluated by
UNLV. It was open-sourced by HP and UNLV in 2005.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/tesseract
