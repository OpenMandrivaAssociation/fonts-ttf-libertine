%define archivename	LinLibertineTTF
%define reldate		2012_07_02
%define fontdir		%{_datadir}/fonts/ttf/libertine

Name:		fonts-ttf-libertine
Version:	5.3.0
Release:	2
Summary:	Linux Libertine Open Fonts
Group:		System/Fonts/True type
License:	GPLv2 and OFL
URL:		https://linuxlibertine.sf.net
Source0:	http://downloads.sourceforge.net/project/linuxlibertine/linuxlibertine/5.3.0/%{archivename}_%{version}_%{reldate}.tgz
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	freetype-tools
Provides:	linux-libertine-fonts
Obsoletes:	linux-libertine-fonts

%description
The Linux Libertine Open Fonts are a TrueType font family for practical
use in documents. They were created to provide a free alternative to
proprietary standard fonts.


%prep
%setup -qc


%install
install -d -m 0755 %{buildroot}%{fontdir}
install -p -m 0644 *.ttf  %{buildroot}%{fontdir}
ttmkfdir -d %{buildroot}%{fontdir} -o %{buildroot}%{fontdir}/fonts.scale
cp -f %{buildroot}%{fontdir}/fonts.scale %{buildroot}%{fontdir}/fonts.dir
mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d
ln -s %{fontdir} %{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-libertine:pri=50


%files
%doc *.txt
%{fontdir}
%{_sysconfdir}/X11/fontpath.d/ttf-libertine:pri=50


%changelog
* Tue Jul 10 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 5.3.0-1mdv2011.0
+ Revision: 808716
- update to 5.3.0

* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 5.0.0-1
+ Revision: 677556
- new version 5.0.0

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 4.4.1-4
+ Revision: 675575
- br fontconfig for fc-query used in new rpm-setup-build

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 4.4.1-3mdv2011.0
+ Revision: 610735
- rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 4.4.1-2mdv2010.1
+ Revision: 494152
- fc-cache is now called by an rpm filetrigger

* Sat Dec 12 2009 Frederik Himpe <fhimpe@mandriva.org> 4.4.1-1mdv2010.1
+ Revision: 477781
- Update to new version 4.4.1

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 2.8.14-2mdv2010.0
+ Revision: 428851
- rebuild

* Wed Jul 30 2008 Funda Wang <fwang@mandriva.org> 2.8.14-1mdv2009.0
+ Revision: 254843
- update doc files
- Use pre-built fonts
- New version 2.8.14

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.7.9-3mdv2009.0
+ Revision: 245282
- rebuild

* Mon Dec 31 2007 Funda Wang <fwang@mandriva.org> 2.7.9-1mdv2008.1
+ Revision: 139763
- New versino 2.7.9

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 04 2007 Adam Williamson <awilliamson@mandriva.org> 2.6.9-1mdv2008.0
+ Revision: 79374
- Import fonts-ttf-libertine

