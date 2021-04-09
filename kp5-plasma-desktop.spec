# TODO:
# PackageKit qt5
#
%define		kdeplasmaver	5.21.4
%define		qtver		5.9.0
%define		kpname		plasma-desktop

Summary:	KDE Plasma Desktop
Name:		kp5-%{kpname}
Version:	5.21.4
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	4a7bc0bb32146f27cc2193d3d261db5a
URL:		http://www.kde.org/
BuildRequires:	AppStream-qt-devel
BuildRequires:	Qt5Concurrent-devel >= %{qtver}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5PrintSupport-devel >= %{qtver}
BuildRequires:	Qt5Sql-devel >= %{qtver}
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	docbook-dtd45-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	fontconfig-devel
BuildRequires:	ibus-devel
BuildRequires:	kf5-attica-devel
BuildRequires:	kf5-baloo-devel
BuildRequires:	kf5-extra-cmake-modules
BuildRequires:	kf5-kactivities-devel
BuildRequires:	kf5-kactivities-stats-devel
BuildRequires:	kf5-karchive-devel
BuildRequires:	kf5-kauth-devel
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-kded-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-kglobalaccel-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-knotifyconfig-devel
BuildRequires:	kf5-kpeople-devel
BuildRequires:	kf5-krunner-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-kwallet-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	kp5-breeze-devel >= %{kdeplasmaver}
BuildRequires:	kp5-kscreenlocker-devel >= %{kdeplasmaver}
BuildRequires:	kp5-kwin-devel >= %{kdeplasmaver}
BuildRequires:	kp5-plasma-workspace-devel
BuildRequires:	libcanberra-devel
BuildRequires:	ninja
BuildRequires:	phonon-qt5-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	scim-devel
BuildRequires:	udev-devel
BuildRequires:	xcb-util-image-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xorg-driver-input-evdev-devel
BuildRequires:	xorg-driver-input-synaptics-devel
BuildRequires:	xorg-lib-libXcursor-devel
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
rm -rf po/id
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build
rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{sr,sr@latin}

%find_lang %{kpname} --all-name --with-kde

sed -i -e 's#/usr/bin/awk#/bin/awk#' $RPM_BUILD_ROOT%{_datadir}/kconf_update/kxkb_variants.awk

find $RPM_BUILD_ROOT%{_datadir}/kconf_update -type f -name "*.py" \
-exec sed -i -e 's#/usr/bin/env python3#/usr/bin/python3#' '{}' +

find $RPM_BUILD_ROOT%{_datadir}/kconf_update -type f -name "*.py" \
-exec sed -i -e 's#/usr/bin/env python#/usr/bin/python3#' '{}' +

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
/etc/xdg/autostart/kaccess.desktop
%attr(755,root,root) %{_bindir}/ibus-ui-emojier-plasma
%attr(755,root,root) %{_bindir}/kaccess
%attr(755,root,root) %{_bindir}/kcm-touchpad-list-devices
%attr(755,root,root) %{_bindir}/knetattach
%attr(755,root,root) %{_bindir}/krunner-plugininstaller
%attr(755,root,root) %{_bindir}/solid-action-desktop-gen
%attr(755,root,root) %{_bindir}/tastenbrett
%attr(755,root,root) %{_libdir}/libkdeinit5_kaccess.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_activities.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_clock.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_desktoppaths.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_formats.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_joystick.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_keyboard.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_plasmasearch.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_solid_actions.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_access.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_autostart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_baloofile.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_componentchooser.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_kded.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_keys.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_launchfeedback.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_nightcolor.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_notifications.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_smserver.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_splashscreen.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_users.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_workspace.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcmspellchecking.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kded_touchpad.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/device_automounter.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/keyboard.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/krunner_kwin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/krunner_plasma-desktop.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libkcm_device_automounter.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libkcm_qtquicksettings.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_touchpad.so
%dir %{_libdir}/qt5/qml/org/kde/activities/settings
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/activities/settings/libkactivitiessettingsplugin.so
%{_libdir}/qt5/qml/org/kde/activities/settings/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/activityswitcher
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/activityswitcher/libactivityswitcherextensionplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/activityswitcher/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/kimpanel
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/kimpanel/libkimpanelplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/kimpanel/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/pager
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/pager/libpagerplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/pager/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/showdesktop
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/showdesktop/libshowdesktopplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/showdesktop/qmldir
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
%attr(755,root,root) %{_prefix}/libexec/kauth/kcmdatetimehelper
%attr(755,root,root) %{_prefix}/libexec/kimpanel-ibus-panel
%attr(755,root,root) %{_prefix}/libexec/kimpanel-ibus-panel-launcher
%attr(755,root,root) %{_prefix}/libexec/kimpanel-scim-panel
%{_desktopdir}/org.kde.knetattach.desktop
%{_desktopdir}/org.kde.plasma.emojier.desktop
%{_datadir}/config.kcfg/kactivitymanagerd_plugins_settings.kcfg
%{_datadir}/config.kcfg/kactivitymanagerd_settings.kcfg
%{_datadir}/config.kcfg/kcmaccessibilitybell.kcfg
%{_datadir}/config.kcfg/kcmaccessibilitykeyboard.kcfg
%{_datadir}/config.kcfg/kcmaccessibilitymouse.kcfg
%{_datadir}/config.kcfg/kcmaccessibilityscreenreader.kcfg
%{_datadir}/config.kcfg/launchfeedbacksettingsbase.kcfg
%{_datadir}/config.kcfg/splashscreensettings.kcfg
%{_datadir}/config.kcfg/touchpad.kcfg
%{_datadir}/config.kcfg/touchpaddaemon.kcfg
%{_datadir}/config.kcfg/workspaceoptions_kdeglobalssettings.kcfg
%{_datadir}/config.kcfg/workspaceoptions_plasmasettings.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.touchpad.xml
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmclock.service
%{_datadir}/dbus-1/system.d/org.kde.kcontrol.kcmclock.conf
%{_iconsdir}/hicolor/128x128/devices/input-touchpad.png
%{_iconsdir}/hicolor/16x16/devices/input-touchpad.png
%{_iconsdir}/hicolor/22x22/devices/input-touchpad.png
%{_iconsdir}/hicolor/24x24/devices/input-touchpad.png
%{_iconsdir}/hicolor/256x256/devices/input-touchpad.png
%{_iconsdir}/hicolor/32x32/devices/input-touchpad.png
%{_iconsdir}/hicolor/48x48/devices/input-touchpad.png
%{_iconsdir}/hicolor/64x64/devices/input-touchpad.png
%{_iconsdir}/hicolor/96x96/devices/input-touchpad.png
%{_iconsdir}/hicolor/scalable/devices/input-touchpad.svgz
%dir %{_datadir}/kcmkeyboard
%dir %{_datadir}/kcmkeyboard/pics
%{_datadir}/kcmkeyboard/pics/epo.png
%dir %{_datadir}/kcmkeys
%{_datadir}/kcmkeys/kde3.kksrc
%{_datadir}/kcmkeys/kde4.kksrc
%{_datadir}/kcmkeys/mac4.kksrc
%{_datadir}/kcmkeys/unix3.kksrc
%{_datadir}/kcmkeys/win3.kksrc
%{_datadir}/kcmkeys/win4.kksrc
%{_datadir}/kcmkeys/wm3.kksrc
%dir %{_datadir}/kcmsolidactions
%{_datadir}/kcmsolidactions/solid-action-template.desktop
%attr(755,root,root) %{_datadir}/kconf_update/kcminputrc_migrate_repeat_value.py
%{_datadir}/kconf_update/kcminputrc_repeat.upd
%attr(755,root,root) %{_datadir}/kconf_update/ksmserver_update_loginMode_value.py
%{_datadir}/kconf_update/ksmserver_update_loginMode_value.upd
%attr(755,root,root) %{_datadir}/kconf_update/kxkb_variants.awk
%{_datadir}/kconf_update/kxkb_variants.upd
%dir %{_datadir}/kf5/kactivitymanagerd
%dir %{_datadir}/kf5/kactivitymanagerd/workspace
%dir %{_datadir}/kf5/kactivitymanagerd/workspace/settings
%dir %{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml
%dir %{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activitiesTab
%dir %{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activityDialog
%dir %{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/privacyTab
%{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activitiesTab/ActivitiesView.qml
%{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activitiesTab/main.qml
%{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activityDialog/GeneralTab.qml
%{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/privacyTab/BlacklistApplicationView.qml
%{_datadir}/kglobalaccel/org.kde.plasma.emojier.desktop
%{_datadir}/knotifications5/kaccess.notifyrc
%{_datadir}/knotifications5/kcm_touchpad.notifyrc
%{_datadir}/knsrcfiles/krunner.knsrc
%{_datadir}/knsrcfiles/ksplash.knsrc
%dir %{_datadir}/kpackage/kcms/kcm5_kded
%dir %{_datadir}/kpackage/kcms/kcm5_kded/contents
%dir %{_datadir}/kpackage/kcms/kcm5_kded/contents/ui
%{_datadir}/kpackage/kcms/kcm5_kded/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm5_kded/metadata.desktop
%{_datadir}/kpackage/kcms/kcm5_kded/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_autostart
%dir %{_datadir}/kpackage/kcms/kcm_autostart/contents
%dir %{_datadir}/kpackage/kcms/kcm_autostart/contents/ui
%{_datadir}/kpackage/kcms/kcm_autostart/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_autostart/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_autostart/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_baloofile
%dir %{_datadir}/kpackage/kcms/kcm_baloofile/contents
%dir %{_datadir}/kpackage/kcms/kcm_baloofile/contents/ui
%{_datadir}/kpackage/kcms/kcm_baloofile/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_baloofile/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_baloofile/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_componentchooser
%dir %{_datadir}/kpackage/kcms/kcm_componentchooser/contents
%dir %{_datadir}/kpackage/kcms/kcm_componentchooser/contents/ui
%{_datadir}/kpackage/kcms/kcm_componentchooser/contents/ui/ComponentComboBox.qml
%{_datadir}/kpackage/kcms/kcm_componentchooser/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_componentchooser/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_componentchooser/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_keys
%dir %{_datadir}/kpackage/kcms/kcm_keys/contents
%dir %{_datadir}/kpackage/kcms/kcm_keys/contents/ui
%{_datadir}/kpackage/kcms/kcm_keys/contents/ui/ShortcutActionDelegate.qml
%{_datadir}/kpackage/kcms/kcm_keys/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_keys/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_keys/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_launchfeedback
%dir %{_datadir}/kpackage/kcms/kcm_launchfeedback/contents
%dir %{_datadir}/kpackage/kcms/kcm_launchfeedback/contents/ui
%{_datadir}/kpackage/kcms/kcm_launchfeedback/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_launchfeedback/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_launchfeedback/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_nightcolor
%dir %{_datadir}/kpackage/kcms/kcm_nightcolor/contents
%dir %{_datadir}/kpackage/kcms/kcm_nightcolor/contents/ui
%{_datadir}/kpackage/kcms/kcm_nightcolor/contents/ui/LocationsFixedView.qml
%{_datadir}/kpackage/kcms/kcm_nightcolor/contents/ui/NumberField.qml
%{_datadir}/kpackage/kcms/kcm_nightcolor/contents/ui/TimeField.qml
%{_datadir}/kpackage/kcms/kcm_nightcolor/contents/ui/TimingsView.qml
%{_datadir}/kpackage/kcms/kcm_nightcolor/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_nightcolor/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_nightcolor/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_notifications
%dir %{_datadir}/kpackage/kcms/kcm_notifications/contents
%dir %{_datadir}/kpackage/kcms/kcm_notifications/contents/ui
%{_datadir}/kpackage/kcms/kcm_notifications/contents/ui/ApplicationConfiguration.qml
%{_datadir}/kpackage/kcms/kcm_notifications/contents/ui/PopupPositionPage.qml
%{_datadir}/kpackage/kcms/kcm_notifications/contents/ui/ScreenPositionSelector.qml
%{_datadir}/kpackage/kcms/kcm_notifications/contents/ui/SourcesPage.qml
%{_datadir}/kpackage/kcms/kcm_notifications/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_notifications/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_notifications/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_smserver
%dir %{_datadir}/kpackage/kcms/kcm_smserver/contents
%dir %{_datadir}/kpackage/kcms/kcm_smserver/contents/ui
%{_datadir}/kpackage/kcms/kcm_smserver/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_smserver/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_smserver/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_splashscreen
%dir %{_datadir}/kpackage/kcms/kcm_splashscreen/contents
%dir %{_datadir}/kpackage/kcms/kcm_splashscreen/contents/ui
%{_datadir}/kpackage/kcms/kcm_splashscreen/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_splashscreen/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_splashscreen/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_users
%dir %{_datadir}/kpackage/kcms/kcm_users/contents
%dir %{_datadir}/kpackage/kcms/kcm_users/contents/ui
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/ChangePassword.qml
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/ChangeWalletPassword.qml
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/CreateUser.qml
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/UserDetailsPage.qml
%{_datadir}/kpackage/kcms/kcm_users/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_users/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_users/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_workspace
%dir %{_datadir}/kpackage/kcms/kcm_workspace/contents
%dir %{_datadir}/kpackage/kcms/kcm_workspace/contents/ui
%{_datadir}/kpackage/kcms/kcm_workspace/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_workspace/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_workspace/metadata.json
%dir %{_datadir}/kpackage/kcms/kcmaccess
%dir %{_datadir}/kpackage/kcms/kcmaccess/contents
%dir %{_datadir}/kpackage/kcms/kcmaccess/contents/ui
%{_datadir}/kpackage/kcms/kcmaccess/contents/ui/Bell.qml
%{_datadir}/kpackage/kcms/kcmaccess/contents/ui/KeyboardFilters.qml
%{_datadir}/kpackage/kcms/kcmaccess/contents/ui/ModifierKeys.qml
%{_datadir}/kpackage/kcms/kcmaccess/contents/ui/MouseNavigation.qml
%{_datadir}/kpackage/kcms/kcmaccess/contents/ui/ScreenReader.qml
%{_datadir}/kpackage/kcms/kcmaccess/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcmaccess/metadata.desktop
%{_datadir}/kpackage/kcms/kcmaccess/metadata.json
%{_datadir}/kservices5/autostart.desktop
%{_datadir}/kservices5/clock.desktop
%{_datadir}/kservices5/componentchooser.desktop
%{_datadir}/kservices5/desktoppath.desktop
%{_datadir}/kservices5/device_automounter_kcm.desktop
%{_datadir}/kservices5/formats.desktop
%{_datadir}/kservices5/joystick.desktop
%{_datadir}/kservices5/kcm_access.desktop
%{_datadir}/kservices5/kcm_activities.desktop
%{_datadir}/kservices5/kcm_baloofile.desktop
%{_datadir}/kservices5/kcm_keyboard.desktop
%{_datadir}/kservices5/kcm_keys.desktop
%{_datadir}/kservices5/kcm_launchfeedback.desktop
%{_datadir}/kservices5/kcm_nightcolor.desktop
%{_datadir}/kservices5/kcm_notifications.desktop
%{_datadir}/kservices5/kcm_plasmasearch.desktop
%{_datadir}/kservices5/kcm_smserver.desktop
%{_datadir}/kservices5/kcm_splashscreen.desktop
%{_datadir}/kservices5/kcm_touchpad.desktop
%{_datadir}/kservices5/kcm_users.desktop
%{_datadir}/kservices5/kcm_workspace.desktop
%{_datadir}/kservices5/kcmkded.desktop
%{_datadir}/kservices5/kded/touchpad.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.icontasks.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.keyboardlayout.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.kicker.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.kickoff.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.kimpanel.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.marginsseparator.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.minimizeall.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.pager.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.showActivityManager.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.showdesktop.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.taskmanager.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.trash.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.windowlist.desktop
%{_datadir}/kservices5/plasma-applet-touchpad.desktop
%{_datadir}/kservices5/plasma-containment-org.kde.desktopcontainment.desktop
%{_datadir}/kservices5/plasma-containment-org.kde.panel.desktop
%{_datadir}/kservices5/plasma-containment-org.kde.plasma.folder.desktop
%{_datadir}/kservices5/plasma-dataengine-touchpad.desktop
%{_datadir}/kservices5/plasma-layout-template-org.kde.plasma.desktop.appmenubar.desktop
%{_datadir}/kservices5/plasma-layout-template-org.kde.plasma.desktop.defaultPanel.desktop
%{_datadir}/kservices5/plasma-layout-template-org.kde.plasma.desktop.emptyPanel.desktop
%{_datadir}/kservices5/plasma-package-org.kde.desktoptoolbox.desktop
%{_datadir}/kservices5/plasma-package-org.kde.paneltoolbox.desktop
%{_datadir}/kservices5/plasma-shell-org.kde.plasma.desktop.desktop
%{_datadir}/kservices5/qtquicksettings.desktop
%{_datadir}/kservices5/solid-actions.desktop
%{_datadir}/kservices5/spellchecking.desktop
%{_datadir}/kservicetypes5/solid-device-type.desktop
%{_datadir}/metainfo/org.kde.desktopcontainment.appdata.xml
%{_datadir}/metainfo/org.kde.desktoptoolbox.appdata.xml
%{_datadir}/metainfo/org.kde.paneltoolbox.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.desktop.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.desktop.appmenubar.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.desktop.defaultPanel.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.desktop.emptyPanel.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.folder.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.icontasks.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.keyboardlayout.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.kicker.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.kickoff.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.kimpanel.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.marginsseparator.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.minimizeall.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.pager.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.showActivityManager.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.showdesktop.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.taskmanager.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.trash.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.windowlist.appdata.xml
%{_datadir}/metainfo/org.kde.plasmashell.metainfo.xml
%{_datadir}/plasma/avatars
%{_datadir}/plasma/desktoptheme/default/icons/touchpad.svg
%dir %{_datadir}/plasma/layout-templates
%dir %{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.appmenubar
%dir %{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.appmenubar/contents
%{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.appmenubar/contents/layout.js
%{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.appmenubar/metadata.desktop
%{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.appmenubar/metadata.json
%dir %{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.defaultPanel
%dir %{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.defaultPanel/contents
%{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.defaultPanel/contents/layout.js
%{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.defaultPanel/metadata.desktop
%{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.defaultPanel/metadata.json
%dir %{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.emptyPanel
%dir %{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.emptyPanel/contents
%{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.emptyPanel/contents/layout.js
%{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.emptyPanel/metadata.desktop
%{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.emptyPanel/metadata.json
%dir %{_datadir}/plasma/packages/org.kde.desktoptoolbox
%dir %{_datadir}/plasma/packages/org.kde.desktoptoolbox/contents
%dir %{_datadir}/plasma/packages/org.kde.desktoptoolbox/contents/config
%dir %{_datadir}/plasma/packages/org.kde.desktoptoolbox/contents/ui
%{_datadir}/plasma/packages/org.kde.desktoptoolbox/contents/config/main.xml
%{_datadir}/plasma/packages/org.kde.desktoptoolbox/contents/ui/ToolBoxButton.qml
%{_datadir}/plasma/packages/org.kde.desktoptoolbox/contents/ui/ToolBoxRoot.qml
%{_datadir}/plasma/packages/org.kde.desktoptoolbox/metadata.desktop
%{_datadir}/plasma/packages/org.kde.desktoptoolbox/metadata.json
%dir %{_datadir}/plasma/packages/org.kde.paneltoolbox
%dir %{_datadir}/plasma/packages/org.kde.paneltoolbox/contents
%dir %{_datadir}/plasma/packages/org.kde.paneltoolbox/contents/ui
%{_datadir}/plasma/packages/org.kde.paneltoolbox/contents/ui/main.qml
%{_datadir}/plasma/packages/org.kde.paneltoolbox/metadata.desktop
%{_datadir}/plasma/packages/org.kde.paneltoolbox/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.desktopcontainment
%dir %{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/config
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/ActionButton.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/BackButtonItem.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/BusyOverlay.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/CompactRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/ConfigFilter.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/ConfigIcons.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/ConfigLocation.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/ConfigOverlay.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/FolderItemActionButton.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/FolderItemDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/FolderItemPreviewPluginsDialog.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/FolderView.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/FolderViewDialog.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/FolderViewDropArea.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/FolderViewLayer.qml
%dir %{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/code
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/code/FolderTools.js
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.panel
%dir %{_datadir}/plasma/plasmoids/org.kde.panel/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.panel/contents/config
%dir %{_datadir}/plasma/plasmoids/org.kde.panel/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.panel/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.panel/contents/ui/ConfigOverlay.qml
%{_datadir}/plasma/plasmoids/org.kde.panel/contents/ui/LayoutManager.js
%{_datadir}/plasma/plasmoids/org.kde.panel/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.panel/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.panel/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.panel/plasma-containment-panel.desktop
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.folder
%{_datadir}/plasma/plasmoids/org.kde.plasma.folder/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.folder/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.icontasks
%{_datadir}/plasma/plasmoids/org.kde.plasma.icontasks/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.icontasks/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardlayout
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardlayout/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardlayout/contents/config
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardlayout/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardlayout/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardlayout/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardlayout/contents/ui/configGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardlayout/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardlayout/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardlayout/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kicker
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/config
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/ui/ActionMenu.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/ui/CompactRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/ui/ConfigGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/ui/DashboardRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/ui/DashboardTabBar.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/ui/DashboardTabButton.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/ui/ItemGridDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/ui/ItemGridView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/ui/ItemListDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/ui/ItemListDialog.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/ui/ItemListView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/ui/ItemMultiGridView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/ui/MenuRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/ui/RunnerResultsList.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/ui/SideBarItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/ui/SideBarSection.qml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/ui/code
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/ui/code/tools.js
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/config
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/ActionMenu.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/ApplicationsGroupView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/ApplicationsView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/BaseView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/Breadcrumb.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/ComputerView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/ConfigGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/FavoritesGridView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/FavoritesView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/FrequentlyUsedView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/FullRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/Header.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/Kickoff.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/KickoffGridItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/KickoffGridView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/KickoffItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/KickoffListView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/LeaveButtons.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/PlacesView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/RecentlyUsedView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/SearchView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/SectionDelegate.qml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/code
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/code/tools.js
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents/config
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents/ui/ActionMenu.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents/ui/CandidateHighlight.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents/ui/ConfigAppearance.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents/ui/ContextMenu.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents/ui/InputPanel.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents/ui/StatusIcon.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.marginsseparator
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.marginsseparator/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.marginsseparator/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.marginsseparator/LICENSE
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.marginsseparator/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.marginsseparator/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.marginsseparator/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.marginsseparator/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.marginsseparator/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.minimizeall
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.minimizeall/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.minimizeall/contents/config
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.minimizeall/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.minimizeall/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.minimizeall/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.minimizeall/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.minimizeall/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.pager
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.pager/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.pager/contents/config
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.pager/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.pager/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.pager/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.pager/contents/ui/configGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.pager/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.pager/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.pager/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.showActivityManager
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.showActivityManager/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.showActivityManager/contents/config
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.showActivityManager/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.showActivityManager/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.showActivityManager/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.showActivityManager/contents/ui/ConfigAppearance.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.showActivityManager/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.showActivityManager/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.showActivityManager/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.showdesktop
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.showdesktop/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.showdesktop/contents/config
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.showdesktop/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.showdesktop/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.showdesktop/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.showdesktop/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.showdesktop/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/config
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/AudioStream.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/Badge.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/ConfigAppearance.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/ConfigBehavior.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/ContextMenu.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/GroupDialog.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/GroupExpanderOverlay.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/MouseHandler.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/PipeWireThumbnail.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/PulseAudio.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/ScrollableTextWrapper.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/Task.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/TaskBadgeOverlay.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/TaskList.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/TaskProgressOverlay.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/ToolTipDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/ToolTipInstance.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/ToolTipWindowMouseArea.qml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/code
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/code/layout.js
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/code/tools.js
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.trash
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.trash/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.trash/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.trash/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.trash/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.trash/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.windowlist
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.windowlist/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.windowlist/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.windowlist/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.windowlist/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.windowlist/metadata.json
%dir %{_datadir}/plasma/plasmoids/touchpad
%dir %{_datadir}/plasma/plasmoids/touchpad/contents
%dir %{_datadir}/plasma/plasmoids/touchpad/contents/ui
%{_datadir}/plasma/plasmoids/touchpad/contents/ui/touchpad.qml
%{_datadir}/plasma/plasmoids/touchpad/metadata.desktop
%{_datadir}/plasma/plasmoids/touchpad/metadata.json
%{_datadir}/plasma/services/touchpad.operations
%dir %{_datadir}/plasma/shells/org.kde.plasma.desktop
%dir %{_datadir}/plasma/shells/org.kde.plasma.desktop/contents
%dir %{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/activitymanager
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/InteractiveConsole.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/activitymanager/ActivityItem.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/activitymanager/ActivityList.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/activitymanager/ActivityManager.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/activitymanager/Heading.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/activitymanager/StoppedActivityItem.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/activitymanager/TaskDropArea.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/activitymanager/WindowPreview.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/activitymanager/static.js
%dir %{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/applet
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/applet/AppletError.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/applet/CompactApplet.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/applet/DefaultCompactRepresentation.qml
%dir %{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration/AboutPlugin.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration/AppletConfiguration.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration/ConfigCategoryDelegate.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration/ConfigurationAppletPage.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration/ConfigurationContainmentActions.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration/ConfigurationContainmentAppearance.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration/ConfigurationKcmPage.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration/ConfigurationShortcuts.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration/ContainmentConfiguration.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration/MouseEventInputButton.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration/PanelConfiguration.qml
%dir %{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration/panelconfiguration
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration/panelconfiguration/EdgeHandle.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration/panelconfiguration/MoreSettingsMenu.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration/panelconfiguration/Ruler.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration/panelconfiguration/SliderHandle.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration/panelconfiguration/ToolBar.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/defaults
%dir %{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/explorer
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/explorer/AppletAlternatives.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/explorer/AppletDelegate.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/explorer/Tooltip.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/explorer/WidgetExplorer.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/layout.js
%dir %{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/updates
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/updates/containmentactions_middlebutton.js
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/updates/maintain_existing_desktop_icon_sizes.js
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/updates/move_desktop_layout_config.js
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/updates/obsolete_kickoffrc.js
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/updates/systemloadviewer_systemmonitor.js
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/updates/unlock_widgets.js
%dir %{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/views
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/views/Desktop.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/views/Panel.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/metadata.desktop
%{_datadir}/plasma/shells/org.kde.plasma.desktop/metadata.json
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmclock.policy
%{_datadir}/qlogging-categories5/kcmkeys.categories
%{_datadir}/qlogging-categories5/kcmusers.categories
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
%attr(755,root,root) %{_libdir}/qt5/plugins/attica_kde.so
%dir %{_datadir}/accounts/providers
%dir %{_datadir}/accounts/providers/kde
%{_datadir}/accounts/providers/kde/opendesktop.provider
%{_datadir}/accounts/services/kde/opendesktop-rating.service
%attr(755,root,root) %{_datadir}/kconf_update/kcminputrc_fix_botched_5_21_0.py
%{_datadir}/kconf_update/kcminputrc_fix_botched_5_21_0.upd
