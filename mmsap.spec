#
# Conditional build:
%bcond_without	alsa	# ALSA sound output
%bcond_without	sdl	# SDL sound output
#
Summary:	Small SAP player for Linux
Summary(pl):	Ma³y odtwarzacz SAP dla Linuksa
Name:		mmsap
# NOTE: check homepage and readme.txt before upgrade (1.4 is preview snapshot atm)
Version:	1.3
Release:	1
License:	GPL
Group:		X11/Applications/Sound
#Source0Download: http://www.baktra.wz.cz/english/mmsap.html
Source0:	http://www.baktra.wz.cz/software/packages/%{name}-%{version}.tar.gz
# Source0-md5:	08fe2ba8991090477671292754d7f92e
URL:		http://www.baktra.wz.cz/english/mmsap.html
BuildRequires:	SDL-devel >= 1.2.10
BuildRequires:	alsa-lib-devel >= 1.0.0
BuildRequires:	gtkmm-devel >= 2.8.0
BuildRequires:	libsap-devel >= 1.54
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small SAP player for Linux. It has GTKmm user interface and for
decoding SAP tunes it uses "SAP library v. 1.54 by Adam Bienias".

%description -l pl
Ma³y odtwarzacz SAP dla Linuksa. Ma interfejs u¿ytkownika GTKmm, a do
dekodowania melodii SAP wykorzystuje bibliotekê SAP w wersji 1.54
autorstwa Adama Bieniasa.

%package SDL
Summary:	Small SAP player for Linux with SDL sound output
Summary(pl):	Ma³y odtwarzacz SAP dla Linuksa z wyj¶ciem d¼wiêku SDL
Group:		X11/Applications/Sound
Requires:	libsap >= 1.54

%description SDL
Small SAP player for Linux. It has GTKmm user interface and for
decoding SAP tunes it uses "SAP library v. 1.54 by Adam Bienias".

This package contains program with SDL sound output.

%description SDL -l pl
Ma³y odtwarzacz SAP dla Linuksa. Ma interfejs u¿ytkownika GTKmm, a do
dekodowania melodii SAP wykorzystuje bibliotekê SAP w wersji 1.54
autorstwa Adama Bieniasa.

Ten pakiet zawiera program z wyj¶ciem d¼wiêku SDL.

%package alsa
Summary:	Small SAP player for Linux with ALSA sound output
Summary(pl):	Ma³y odtwarzacz SAP dla Linuksa z wyj¶ciem d¼wiêku ALSA
Group:		X11/Applications/Sound
Requires:	libsap >= 1.54

%description alsa
Small SAP player for Linux. It has GTKmm user interface and for
decoding SAP tunes it uses "SAP library v. 1.54 by Adam Bienias".

This package contains program with ALSA sound output.

%description alsa -l pl
Ma³y odtwarzacz SAP dla Linuksa. Ma interfejs u¿ytkownika GTKmm, a do
dekodowania melodii SAP wykorzystuje bibliotekê SAP w wersji 1.54
autorstwa Adama Bieniasa.

Ten pakiet zawiera program z wyj¶ciem d¼wiêku ALSA.

%prep
%setup -q

# kill precompiled objects
rm -f libsap/* mmsap-als mmsap-sdl
ln -sf /usr/include/libsap.h libsap/sapLib.h

%build
%if %{with sdl}
echo "#define MMSAP_SOUND_SYSTEM_SDL" > mmsap_config.h
echo '#define MMSAP_VERSION "Version 1.3-SDL"' >> mmsap_config.h
%{__cxx} %{rpmldflags} %{rpmcxxflags} -o mmsap-sdl mmsap.cpp -lSDL `pkg-config gtkmm-2.4 --libs --cflags` -lsap
%endif

%if %{with alsa}
echo "#define MMSAP_SOUND_SYSTEM_ALSA" > mmsap_config.h
echo '#define MMSAP_VERSION "Version 1.3-ALSA"' >> mmsap_config.h
%{__cxx} %{rpmldflags} %{rpmcxxflags} -o mmsap-als mmsap.cpp -lasound `pkg-config gtkmm-2.4 --libs --cflags` -lsap
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%if %{with sdl}
install mmsap-sdl $RPM_BUILD_ROOT%{_bindir}
%endif

%if %{with alsa}
install mmsap-als $RPM_BUILD_ROOT%{_bindir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with sdl}
%files SDL
%defattr(644,root,root,755)
%doc changelog.txt libsap-license.txt readme.txt
%lang(cs) %doc readme_cs.txt
%attr(755,root,root) %{_bindir}/mmsap-sdl
%endif

%if %{with alsa}
%files alsa
%defattr(644,root,root,755)
%doc changelog.txt libsap-license.txt readme.txt
%lang(cs) %doc readme_cs.txt
%attr(755,root,root) %{_bindir}/mmsap-als
%endif
