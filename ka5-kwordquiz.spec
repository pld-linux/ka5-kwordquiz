%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		kwordquiz
Summary:	kwordquiz
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	2daf7c1b0419d40957a85a5adfc07f26
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkeduvocdocument-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.30.0
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcrash-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-kguiaddons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kitemviews-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-knotifyconfig-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kf5-kxmlgui-devel
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

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kwordquiz.knsrc
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
%{_datadir}/knotifications5/kwordquiz.notifyrc
%{_datadir}/kwordquiz
%dir %{_datadir}/kxmlgui5/kwordquiz
%{_datadir}/kxmlgui5/kwordquiz/kwordquizui.rc
%{_datadir}/metainfo/org.kde.kwordquiz.appdata.xml
