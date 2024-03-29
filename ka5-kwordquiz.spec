#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kwordquiz
Summary:	kwordquiz
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	38efff45f151d2cf7d9ca834b48e937c
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkeduvocdocument-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kguiaddons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kitemviews-devel >= %{kframever}
BuildRequires:	kf5-knewstuff-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-knotifyconfig-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	phonon-qt5-devel >= 4.6.60
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-qtdeclarative >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KWordQuiz is the KDE version of the Windows program WordQuiz. If you
have just switched to KDE/Linux you can use all files created in
WordQuiz with KWordQuiz. Additional information about KWordQuiz is
available at the author's own website.

%description -l pl.UTF-8
KWordQuiz jest wersją KDE Windowsowego programu WordQuiz. Jeśli
właśnie przeszedłeś na KDE/Linux możesz użyć wszystkich plików
utworzonych w WordQuiz na KWordQuiz. Więcej informacji o KWordQuiz
znajdziesz na stronie internetowej autora.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build
rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/ko

%find_lang %{kaname} --all-name --with-kde --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwordquiz
%{_desktopdir}/org.kde.kwordquiz.desktop
%{_datadir}/config.kcfg/kwordquiz.kcfg
%{_iconsdir}/hicolor/128x128/apps/kwordquiz.png
%{_iconsdir}/hicolor/128x128/mimetypes/application-x-kwordquiz.png
%{_iconsdir}/hicolor/16x16/apps/kwordquiz.png
%{_iconsdir}/hicolor/16x16/mimetypes/application-x-kwordquiz.png
%{_iconsdir}/hicolor/22x22/apps/kwordquiz.png
%{_iconsdir}/hicolor/22x22/mimetypes/application-x-kwordquiz.png
%{_iconsdir}/hicolor/32x32/apps/kwordquiz.png
%{_iconsdir}/hicolor/32x32/mimetypes/application-x-kwordquiz.png
%{_iconsdir}/hicolor/48x48/apps/kwordquiz.png
%{_iconsdir}/hicolor/48x48/mimetypes/application-x-kwordquiz.png
%{_iconsdir}/hicolor/64x64/apps/kwordquiz.png
%{_iconsdir}/hicolor/scalable/apps/org.kde.kwordquiz.svg
%{_datadir}/knotifications5/kwordquiz.notifyrc
%{_datadir}/kwordquiz
%{_datadir}/metainfo/org.kde.kwordquiz.appdata.xml
%{_datadir}/knsrcfiles/kwordquiz.knsrc
