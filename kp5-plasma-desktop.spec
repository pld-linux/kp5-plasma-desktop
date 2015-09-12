# TODO:
# PackageKit qt5
#
%define		kdeplasmaver	5.4.0
%define		qtver		5.3.2
%define		kpname		plasma-desktop

Summary:	KDE Plasma Desktop
Name:		kp5-%{kpname}
Version:	5.4.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	105aa6d93f32ad99b7afa0c7674aa795
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	fontconfig-devel
BuildRequires:	kf5-attica-devel
BuildRequires:	kf5-kauth-devel
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-kglobalaccel-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-knotifyconfig-devel
BuildRequires:	kf5-kpeople-devel
BuildRequires:	kf5-krunner-devel
BuildRequires:	kf5-kwallet-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xorg-driver-input-evdev-devel
BuildRequires:	xorg-driver-input-synaptics-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KDE Plasma Desktop.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaccess
%attr(755,root,root) %{_bindir}/kapplymousetheme
%attr(755,root,root) %{_bindir}/kcm-touchpad-list-devices
%attr(755,root,root) %{_bindir}/kfontinst
%attr(755,root,root) %{_bindir}/kfontview
%attr(755,root,root) %{_bindir}/knetattach
%attr(755,root,root) %{_bindir}/krdb
%attr(755,root,root) %{_bindir}/solid-action-desktop-gen
%attr(755,root,root) %{_libdir}/kauth/fontinst
%attr(755,root,root) %{_libdir}/kauth/fontinst_helper
%attr(755,root,root) %{_libdir}/kauth/fontinst_x11
%attr(755,root,root) %{_libdir}/kauth/kcmdatetimehelper
%attr(755,root,root) %{_libdir}/kconf_update_bin/krdb_clearlibrarypath
%attr(755,root,root) %{_libdir}/kfontprint
%attr(755,root,root) %{_libdir}/libKF5ActivitiesExperimentalStats.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5ActivitiesExperimentalStats.so.1
%attr(755,root,root) %{_libdir}/libkdeinit5_kaccess.so
%attr(755,root,root) %ghost %{_libdir}/libkfontinst.so.5
%attr(755,root,root) %{_libdir}/libkfontinst.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkfontinstui.so.5
%attr(755,root,root) %{_libdir}/libkfontinstui.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/attica_kde.so
%attr(755,root,root) %{_libdir}/qt5/plugins/fontthumbnail.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_access.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_autostart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_baloofile.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_clock.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_colors.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_componentchooser.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_cursortheme.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_desktoppaths.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_desktoptheme.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_emoticons.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_fontinst.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_fonts.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_formats.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_icons.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_input.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_joystick.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kded.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_keyboard.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_keys.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_knotify.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_launch.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_phonon.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_plasmasearch.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_smserver.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_solid_actions.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_standard_actions.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_style.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_workspaceoptions.so
%dir %{_libdir}/qt5/plugins/kcms
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_lookandfeel.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_splashscreen.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcmspellchecking.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kded_keyboard.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kded_touchpad.so
%attr(755,root,root) %{_libdir}/qt5/plugins/keyboard_layout_widget.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kfontviewpart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kio_fonts.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libkcm_translations.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_touchpad.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/activityswitcher
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/activityswitcher/libactivityswitcherextensionplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/activityswitcher/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/kicker
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/kicker/libkickerplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/kicker/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/kickoff
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/kickoff/libkickoffplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/kickoff/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/pager
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/pager/libpagerplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/pager/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/taskmanager
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/taskmanager/libtaskmanagerplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/taskmanager/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/trash
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/trash/libtrashplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/trash/qmldir
%dir %{_libdir}/qt5/qml/org/kde/private/desktopcontainment
%dir %{_libdir}/qt5/qml/org/kde/private/desktopcontainment/desktop
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/private/desktopcontainment/desktop/libdesktopplugin.so
%{_libdir}/qt5/qml/org/kde/private/desktopcontainment/desktop/qmldir
%dir %{_libdir}/qt5/qml/org/kde/private/desktopcontainment/folder
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/private/desktopcontainment/folder/libfolderplugin.so
%{_libdir}/qt5/qml/org/kde/private/desktopcontainment/folder/qmldir
%{_desktopdir}/org.kde.kfontview.desktop
%{_desktopdir}/org.kde.knetattach.desktop
%dir %{_datadir}/color-schemes
%{_datadir}/color-schemes/Honeycomb.colors
%{_datadir}/color-schemes/Norway.colors
%{_datadir}/color-schemes/ObsidianCoast.colors
%{_datadir}/color-schemes/Oxygen.colors
%{_datadir}/color-schemes/OxygenCold.colors
%{_datadir}/color-schemes/Steel.colors
%{_datadir}/color-schemes/WontonSoup.colors
%{_datadir}/color-schemes/Zion.colors
%{_datadir}/color-schemes/ZionReversed.colors
%{_datadir}/config.kcfg/touchpad.kcfg
%{_datadir}/config.kcfg/touchpaddaemon.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.touchpad.xml
%{_datadir}/dbus-1/services/org.kde.fontinst.service
%{_datadir}/dbus-1/system-services/org.kde.fontinst.service
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmclock.service
%{_iconsdir}/hicolor/*/devices/input-touchpad.png
%{_iconsdir}/hicolor/*/mimetypes/fonts-package.png
%{_iconsdir}/hicolor/*/apps/kfontview.png
%{_iconsdir}/hicolor/scalable/apps/preferences-desktop-font-installer.svgz
%{_iconsdir}/hicolor/scalable/devices/input-touchpad.svgz
%{_datadir}/kcm_componentchooser
%{_datadir}/kcm_phonon
%{_datadir}/kcminput
%{_datadir}/kcmkeyboard
%{_datadir}/kcmkeys
%{_datadir}/kcmsolidactions
%{_datadir}/kconf_update/krdb_libpathwipe.upd
%{_datadir}/kcontrol
%{_datadir}/kdisplay
%{_datadir}/kdm
%{_datadir}/kfontinst
%{_datadir}/knotifications5/kaccess.notifyrc
%{_datadir}/knotifications5/kcm_touchpad.notifyrc
%{_datadir}/knotifications5/kcmstyle.notifyrc
%{_datadir}/konqsidebartng
%{_datadir}/kpackage
%{_datadir}/kservices5/ServiceMenus/installfont.desktop
%{_datadir}/kservices5/autostart.desktop
%{_datadir}/kservices5/clock.desktop
%{_datadir}/kservices5/colors.desktop
%{_datadir}/kservices5/componentchooser.desktop
%{_datadir}/kservices5/cursortheme.desktop
%{_datadir}/kservices5/desktoppath.desktop
%{_datadir}/kservices5/desktoptheme.desktop
%{_datadir}/kservices5/emoticons.desktop
%{_datadir}/kservices5/fontinst.desktop
%{_datadir}/kservices5/fonts.desktop
%{_datadir}/kservices5/fonts.protocol
%{_datadir}/kservices5/fontthumbnail.desktop
%{_datadir}/kservices5/formats.desktop
%{_datadir}/kservices5/icons.desktop
%{_datadir}/kservices5/joystick.desktop
%{_datadir}/kservices5/kaccess.desktop
%{_datadir}/kservices5/kcm_baloofile.desktop
%{_datadir}/kservices5/kcm_keyboard.desktop
%{_datadir}/kservices5/kcm_lookandfeel.desktop
%{_datadir}/kservices5/kcm_phonon.desktop
%{_datadir}/kservices5/kcm_plasmasearch.desktop
%{_datadir}/kservices5/kcm_splashscreen.desktop
%{_datadir}/kservices5/kcm_touchpad.desktop
%{_datadir}/kservices5/kcmaccess.desktop
%{_datadir}/kservices5/kcmkded.desktop
%{_datadir}/kservices5/kcmlaunch.desktop
%{_datadir}/kservices5/kcmnotify.desktop
%{_datadir}/kservices5/kcmsmserver.desktop
%{_datadir}/kservices5/kded/keyboard.desktop
%{_datadir}/kservices5/kded/touchpad.desktop
%{_datadir}/kservices5/keys.desktop
%{_datadir}/kservices5/kfontviewpart.desktop
%{_datadir}/kservices5/mouse.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.folder.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.icontasks.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.kicker.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.kickoff.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.pager.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.showActivityManager.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.taskmanager.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.trash.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.windowlist.desktop
%{_datadir}/kservices5/plasma-applet-touchpad.desktop
%{_datadir}/kservices5/plasma-containment-org.kde.desktopcontainment.desktop
%{_datadir}/kservices5/plasma-containment-org.kde.panel.desktop
%{_datadir}/kservices5/plasma-dataengine-touchpad.desktop
%{_datadir}/kservices5/plasma-layout-template-org.kde.plasma.desktop.defaultPanel.desktop
%{_datadir}/kservices5/plasma-package-org.kde.desktoptoolbox.desktop
%{_datadir}/kservices5/plasma-package-org.kde.paneltoolbox.desktop
%{_datadir}/kservices5/plasma-shell-org.kde.plasma.desktop.desktop
%{_datadir}/kservices5/solid-actions.desktop
%{_datadir}/kservices5/spellchecking.desktop
%{_datadir}/kservices5/standard_actions.desktop
%{_datadir}/kservices5/style.desktop
%{_datadir}/kservices5/translations.desktop
%{_datadir}/kservices5/workspaceoptions.desktop
%{_datadir}/kservicetypes5/solid-device-type.desktop
%dir %{_datadir}/ksmserver/windowmanagers
%{_datadir}/ksmserver/windowmanagers/compiz-custom.desktop
%{_datadir}/ksmserver/windowmanagers/compiz.desktop
%{_datadir}/ksmserver/windowmanagers/metacity.desktop
%{_datadir}/ksmserver/windowmanagers/openbox.desktop
%{_datadir}/kxmlgui5/kfontinst
%{_datadir}/kxmlgui5/kfontview
%{_datadir}/plasma/desktoptheme/default
%dir %{_datadir}/plasma/layout-templates
%{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.defaultPanel
%dir %{_datadir}/plasma/packages
%{_datadir}/plasma/packages/org.kde.desktoptoolbox
%{_datadir}/plasma/packages/org.kde.paneltoolbox
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment
%{_datadir}/plasma/plasmoids/org.kde.panel
%{_datadir}/plasma/plasmoids/org.kde.plasma.folder
%{_datadir}/plasma/plasmoids/org.kde.plasma.icontasks
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff
%{_datadir}/plasma/plasmoids/org.kde.plasma.pager
%{_datadir}/plasma/plasmoids/org.kde.plasma.showActivityManager
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager
%{_datadir}/plasma/plasmoids/org.kde.plasma.trash
%{_datadir}/plasma/plasmoids/org.kde.plasma.windowlist
%{_datadir}/plasma/plasmoids/touchpad
%{_datadir}/plasma/services/touchpad.operations
%dir %{_datadir}/plasma/shells
%{_datadir}/plasma/shells/org.kde.plasma.desktop
%{_datadir}/polkit-1/actions/org.kde.fontinst.policy
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmclock.policy
%dir %{_datadir}/solid/devices
%{_datadir}/solid/devices/solid-device-Battery.desktop
%{_datadir}/solid/devices/solid-device-Block.desktop
%{_datadir}/solid/devices/solid-device-Camera.desktop
%{_datadir}/solid/devices/solid-device-OpticalDisc.desktop
%{_datadir}/solid/devices/solid-device-OpticalDrive.desktop
%{_datadir}/solid/devices/solid-device-PortableMediaPlayer.desktop
%{_datadir}/solid/devices/solid-device-Processor.desktop
%{_datadir}/solid/devices/solid-device-StorageAccess.desktop
%{_datadir}/solid/devices/solid-device-StorageDrive.desktop
%{_datadir}/solid/devices/solid-device-StorageVolume.desktop
/etc/dbus-1/system.d/org.kde.fontinst.conf
/etc/dbus-1/system.d/org.kde.kcontrol.kcmclock.conf
/etc/xdg/colorschemes.knsrc
/etc/xdg/emoticons.knsrc
/etc/xdg/icons.knsrc
/etc/xdg/kfontinst.knsrc
/etc/xdg/plasma-themes.knsrc
/etc/xdg/xcursor.knsrc
