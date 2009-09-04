%define name gshowtv
%define oname GShowTV
%define version 1.2.2
%define release %mkrel 4

Name: %{name}
Summary: %{oname} - A Gnome TV Guide
Version: %{version}
Release: %{release}
Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL: http://gshowtv.sourceforge.net/
License: GPL
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
BuildRequires: perl-Gtk2
BuildRequires: perl(Locale::TextDomain)
BuildRequires: desktop-file-utils
Requires: xmltv-druid
Requires: perl-%{oname}

%package -n perl-%{oname}
Summary: Perl module used by %{oname}
License: GPL
Group: Development/GNOME and GTK+
Requires: perl-Gtk2
Requires: perl(Locale::TextDomain)

%description
%{oname} is a TV program schedule viewer and a Personal Video Recorder GUI.

%{oname}'s basic purpose is to provide a nice GUI for viewing tv program 
schedule information and for recording the programs. GShow TV doesn't itself 
do the recording of the selected programs, rather it uses any PVR solution 
that exists. GShow TV is globally usable as it uses XMLTV to access the 
program schedules, and xmltv has support for multitude of countries.

%description -n perl-%{oname}
%{oname} uses this perl module in its script.

%prep
%setup -n %{name} -q
perl -pi -e "s|.png||" %{name}.desktop

%build
perl Makefile.PL PREFIX=/usr \
 INSTALLSITESCRIPT=%{_bindir} \
 INSTALLSITEMAN1DIR=%{_mandir}/1 \
 INSTALLSITELIB=%{perl_vendorlib}

%make
										
%install
rm -rf %{buildroot}
%makeinstall DESTDIR=%{buildroot}

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="AudioVideo" \
  --remove-key="Encoding" \
  --add-category="GTK" \
  --add-category="X-MandrivaLinux-Multimedia-Video" \
  --dir %{buildroot}%{_datadir}/applications/ \
  %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS KNOWN_ISSUES README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/gnome/help/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/1/%{name}.*

%files -n perl-%{oname}
%doc AUTHORS KNOWN_ISSUES README TODO
%{perl_vendorlib}/%{oname}

