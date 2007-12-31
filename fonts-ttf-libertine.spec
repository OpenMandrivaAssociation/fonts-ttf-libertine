%define archivename	LinLibertineSRC
%define fontdir		%{_datadir}/fonts/ttf/libertine
%define fver		2.7

Name:		fonts-ttf-libertine
Version:	%fver.9
Release:	%mkrel 1
Summary:	Linux Libertine Open Fonts
Group:		System/Fonts/True type
License:	GPL+ and OFL
URL:		http://linuxlibertine.sf.net
Source:		http://dl.sf.net/linuxlibertine/%{archivename}-%{fver}.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch
BuildRequires:	fontforge
BuildRequires:	freetype-tools
Requires(post):	fontconfig
Provides:	linux-libertine-fonts
Obsoletes:	linux-libertine-fonts

%description
The Linux Libertine Open Fonts are a TrueType font family for practical
use in documents. They were created to provide a free alternative to
proprietary standard fonts.


%prep
%setup -q -n %{archivename}


%build
fontforge -script "-" *.sfd <<EOF
i = 1
while ( i < \$argc )
  Open (\$argv[i], 1)
  Generate (\$fontname + ".ttf")
  PrintSetup (5)
  PrintFont (0, 0, "", \$fontname + "-sample.pdf")
  Close()
  i++
endloop
EOF


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


%post
if [ -x %{_bindir}/fc-cache ]; then
  %{_bindir}/fc-cache %{_datadir}/fonts
fi


%postun
if [ "$1" = "0" ]; then
  if [ -x %{_bindir}/fc-cache ]; then
    %{_bindir}/fc-cache %{_datadir}/fonts
  fi
fi


%files
%defattr(644,root,root,755)
%doc Bugs Readme ChangeLog.txt LICENCE.txt *.pdf
%{fontdir}
%{_sysconfdir}/X11/fontpath.d/ttf-libertine:pri=50

