%define name gshowtv
%define oname GShowTV
%define version 1.2.2
%define release 5

Name: %{name}
Summary: %{oname} - A Gnome TV Guide
Version: %{version}
Release: %{release}
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL: http://gshowtv.sourceforge.net/
License: GPL
Group: Graphical desktop/GNOME
BuildArch: noarch
BuildRequires: perl-Gtk2
BuildRequires: perl(Locale::TextDomain)
BuildRequires: desktop-file-utils
buildrequires:	perl-devel
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
schedule information and for recording the programs. GShow TV doesnt itself 
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



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-5mdv2011.0
+ Revision: 619260
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.2.2-4mdv2010.0
+ Revision: 429329
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.2.2-3mdv2009.0
+ Revision: 246660
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Guillaume Bedot <littletux@mandriva.org>
    - is a GTK app
    - Fix requires
    - Fix typo in summary

* Tue Dec 11 2007 Guillaume Bedot <littletux@mandriva.org> 1.2.2-1mdv2008.1
+ Revision: 117187
- First package of gshowtv for Mandriva Linux.
- create gshowtv

