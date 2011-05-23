%define archivename	LinLibertineTTF
%define fontdir		%{_datadir}/fonts/ttf/libertine

Name:		fonts-ttf-libertine
Version:	5.0.0
Release:	%mkrel 1
Summary:	Linux Libertine Open Fonts
Group:		System/Fonts/True type
License:	GPL+ and OFL
URL:		http://linuxlibertine.sf.net
Source:		http://dl.sf.net/linuxlibertine/LinLibertineTTF_2011_05_22.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch
BuildRequires: fontconfig
BuildRequires:	freetype-tools
Provides:	linux-libertine-fonts
Obsoletes:	linux-libertine-fonts

%description
The Linux Libertine Open Fonts are a TrueType font family for practical
use in documents. They were created to provide a free alternative to
proprietary standard fonts.


%prep
%setup -qcn LinLibertineTTF_2011_05_22


%install
rm -rf %{buildroot}

install -d -m 0755 %{buildroot}%{fontdir}
install -p -m 0644 *.ttf  %{buildroot}%{fontdir}
ttmkfdir -d %{buildroot}%{fontdir} -o %{buildroot}%{fontdir}/fonts.scale
cp -f %{buildroot}%{fontdir}/fonts.scale %{buildroot}%{fontdir}/fonts.dir
mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d
ln -s %{fontdir} %{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-libertine:pri=50

%clean
rm -rf %{buildroot}


%files
%defattr(644,root,root,755)
%doc *.txt
%{fontdir}
%{_sysconfdir}/X11/fontpath.d/ttf-libertine:pri=50

