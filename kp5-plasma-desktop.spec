#
# Conditional build:
%bcond_with	tests		# build with tests
# TODO:
# PackageKit qt5
#
%define		kdeplasmaver	5.25.0
%define		qtver		5.9.0
%define		kpname		plasma-desktop

Summary:	KDE Plasma Desktop
Name:		kp5-%{kpname}
Version:	5.25.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	2dac1205e5fb46c3f55a4f222edd8031
URL:		https://www.kde.org/
BuildRequires:	AppStream-qt-devel
BuildRequires:	Qt5Concurrent-devel >= %{qtver}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5PrintSupport-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5Sql-devel >= %{qtver}
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	Qt5X11Extras-devel >= %{qtver}
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	docbook-dtd45-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	fontconfig-devel
BuildRequires:	ibus-devel
BuildRequires:	ka5-kaccounts-integration-devel
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
BuildRequires:	kf5-kirigami2-devel
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
BuildRequires:	kf5-qqc2-desktop-style-devel
BuildRequires:	kp5-breeze-devel >= %{kdeplasmaver}
BuildRequires:	kp5-kscreenlocker-devel >= %{kdeplasmaver}
BuildRequires:	kp5-kwin-devel >= %{kdeplasmaver}
BuildRequires:	kp5-libksysguard-devel >= %{kdeplasmaver}
BuildRequires:	kp5-plasma-workspace-devel >= %{kdeplasmaver}
BuildRequires:	libaccounts-qt5-devel
BuildRequires:	libcanberra-devel
BuildRequires:	libsignon-qt5-devel
BuildRequires:	ninja
BuildRequires:	phonon-qt5-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	scim-devel
BuildRequires:	udev-devel
BuildRequires:	xcb-util-image-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xkeyboard-config
BuildRequires:	xorg-driver-input-evdev-devel
BuildRequires:	xorg-driver-input-libinput-devel
BuildRequires:	xorg-driver-input-synaptics-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-xserver-server-devel
BuildRequires:	xz
Requires:	/bin/awk
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
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	../
%ninja_build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build
rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{sr,sr@latin}

%find_lang %{kpname} --all-name --with-kde

find $RPM_BUILD_ROOT%{_datadir}/kconf_update -type f -name "*.awk" \
-exec sed -i -e 's#/usr/bin/awk#/bin/awk#' '{}' +

sed -i -e 's#/usr/bin/env bash#/bin/bash#' $RPM_BUILD_ROOT%{_datadir}/kconf_update/kcm_rename_plasma_desktop.sh

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
%attr(755,root,root) %{_bindir}/kapplymousetheme
%attr(755,root,root) %{_bindir}/kcm-touchpad-list-devices
%attr(755,root,root) %{_bindir}/knetattach
%attr(755,root,root) %{_bindir}/krunner-plugininstaller
%attr(755,root,root) %{_bindir}/solid-action-desktop-gen
%attr(755,root,root) %{_bindir}/tastenbrett
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/device_automounter.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/keyboard.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/krunner_kwin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/krunner_plasma-desktop.so
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
%{_datadir}/kpackage/kcms/kcm5_kded
%{_datadir}/kpackage/kcms/kcm_baloofile
%{_datadir}/kpackage/kcms/kcm_componentchooser
%{_datadir}/kpackage/kcms/kcm_keys
%{_datadir}/kpackage/kcms/kcm_launchfeedback
%{_datadir}/kpackage/kcms/kcm_smserver
%{_datadir}/kpackage/kcms/kcm_splashscreen
%{_datadir}/kpackage/kcms/kcm_workspace
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
%dir %{_datadir}/plasma/layout-templates
%dir %{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.appmenubar
%dir %{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.appmenubar/contents
%{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.appmenubar/contents/layout.js
%{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.appmenubar/metadata.json
%dir %{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.defaultPanel
%dir %{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.defaultPanel/contents
%{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.defaultPanel/contents/layout.js
%{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.defaultPanel/metadata.json
%dir %{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.emptyPanel
%dir %{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.emptyPanel/contents
%{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.emptyPanel/contents/layout.js
%{_datadir}/plasma/layout-templates/org.kde.plasma.desktop.emptyPanel/metadata.json
%dir %{_datadir}/plasma/packages/org.kde.desktoptoolbox
%dir %{_datadir}/plasma/packages/org.kde.desktoptoolbox/contents
%dir %{_datadir}/plasma/packages/org.kde.desktoptoolbox/contents/config
%dir %{_datadir}/plasma/packages/org.kde.desktoptoolbox/contents/ui
%{_datadir}/plasma/packages/org.kde.desktoptoolbox/contents/config/main.xml
%{_datadir}/plasma/packages/org.kde.desktoptoolbox/contents/ui/ToolBoxRoot.qml
%{_datadir}/plasma/packages/org.kde.desktoptoolbox/metadata.json
%dir %{_datadir}/plasma/packages/org.kde.paneltoolbox
%dir %{_datadir}/plasma/packages/org.kde.paneltoolbox/contents
%dir %{_datadir}/plasma/packages/org.kde.paneltoolbox/contents/ui
%{_datadir}/plasma/packages/org.kde.paneltoolbox/contents/ui/main.qml
%{_datadir}/plasma/packages/org.kde.paneltoolbox/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment
%{_datadir}/plasma/plasmoids/org.kde.panel
%{_datadir}/plasma/plasmoids/org.kde.plasma.folder
%{_datadir}/plasma/plasmoids/org.kde.plasma.icontasks
%{_datadir}/plasma/plasmoids/org.kde.plasma.keyboardlayout
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel
%{_datadir}/plasma/plasmoids/org.kde.plasma.marginsseparator
%{_datadir}/plasma/plasmoids/org.kde.plasma.minimizeall
%{_datadir}/plasma/plasmoids/org.kde.plasma.pager
%{_datadir}/plasma/plasmoids/org.kde.plasma.showActivityManager
%{_datadir}/plasma/plasmoids/org.kde.plasma.showdesktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager
%{_datadir}/plasma/plasmoids/org.kde.plasma.trash
%{_datadir}/plasma/plasmoids/org.kde.plasma.windowlist
%{_datadir}/plasma/shells/org.kde.plasma.desktop
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmclock.policy
%{_datadir}/qlogging-categories5/kcmkeys.categories
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

%dir %{_libdir}/qt5/qml/org/kde/plasma/emoji
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/emoji/libEmojierDeclarativePlugin.so
%{_libdir}/qt5/qml/org/kde/plasma/emoji/qmldir
%{_datadir}/config.kcfg/landingpage_kdeglobalssettings.kcfg
%dir %{_datadir}/kpackage/kcms/kcm_landingpage
%dir %{_datadir}/kpackage/kcms/kcm_landingpage/contents
%dir %{_datadir}/kpackage/kcms/kcm_landingpage/contents/ui
%{_datadir}/kpackage/kcms/kcm_landingpage/contents/ui/FeedbackControls.qml
%{_datadir}/kpackage/kcms/kcm_landingpage/contents/ui/MostUsedIcon.qml
%{_datadir}/kpackage/kcms/kcm_landingpage/contents/ui/Thumbnail.qml
%{_datadir}/kpackage/kcms/kcm_landingpage/contents/ui/main.qml
%{_datadir}/qlogging-categories5/kcm_kded.categories
%{_datadir}/qlogging-categories5/kcm_keyboard.categories
%{_libdir}/qt5/plugins/kf5/kded/kded_touchpad.so
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff
%{_datadir}/plasma/services/touchpad.operations
%{_datadir}/plasma/desktoptheme/default/icons/touchpad.svg
%{_datadir}/plasma/plasmoids/touchpad

%dir %{_libdir}/qt5/plugins/plasma/kcminit
%{_libdir}/qt5/plugins/plasma/kcminit/kcm_mouse_init.so
%{_libdir}/qt5/plugins/plasma/kcminit/kcm_touchpad_init.so
%dir %{_libdir}/qt5/plugins/plasma/kcms
%dir %{_libdir}/qt5/plugins/plasma/kcms/systemsettings
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_access.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_baloofile.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_componentchooser.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_kded.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_keyboard.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_keys.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_landingpage.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_launchfeedback.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_mouse.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_smserver.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_splashscreen.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_tablet.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_touchpad.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_workspace.so
%dir %{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_activities.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_clock.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_desktoppaths.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_device_automounter.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_joystick.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_plasmasearch.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_qtquicksettings.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_solid_actions.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcmspellchecking.so
%{_desktopdir}/kcm_access.desktop
%{_desktopdir}/kcm_activities.desktop
%{_desktopdir}/kcm_baloofile.desktop
%{_desktopdir}/kcm_clock.desktop
%{_desktopdir}/kcm_componentchooser.desktop
%{_desktopdir}/kcm_desktoppaths.desktop
%{_desktopdir}/kcm_device_automounter.desktop
%{_desktopdir}/kcm_joystick.desktop
%{_desktopdir}/kcm_kded.desktop
%{_desktopdir}/kcm_keyboard.desktop
%{_desktopdir}/kcm_keys.desktop
%{_desktopdir}/kcm_launchfeedback.desktop
%{_desktopdir}/kcm_mouse.desktop
%{_desktopdir}/kcm_plasmasearch.desktop
%{_desktopdir}/kcm_qtquicksettings.desktop
%{_desktopdir}/kcm_smserver.desktop
%{_desktopdir}/kcm_solid_actions.desktop
%{_desktopdir}/kcm_splashscreen.desktop
%{_desktopdir}/kcm_tablet.desktop
%{_desktopdir}/kcm_touchpad.desktop
%{_desktopdir}/kcm_workspace.desktop
%{_desktopdir}/kcmspellchecking.desktop
%attr(755,root,root) %{_datadir}/kconf_update/kcm_rename_plasma_desktop.sh
%{_datadir}/kconf_update/kcm_rename_plasma_desktop.upd
%{_datadir}/kconf_update/kxkb.upd
%attr(755,root,root) %{_datadir}/kconf_update/kxkb_emptylists.awk
%attr(755,root,root) %{_datadir}/kconf_update/kxkb_resetoptions.awk
%dir %{_datadir}/kpackage/kcms/kcm_access
%dir %{_datadir}/kpackage/kcms/kcm_access/contents
%dir %{_datadir}/kpackage/kcms/kcm_access/contents/ui
%{_datadir}/kpackage/kcms/kcm_access/contents/ui/Bell.qml
%{_datadir}/kpackage/kcms/kcm_access/contents/ui/KeyboardFilters.qml
%{_datadir}/kpackage/kcms/kcm_access/contents/ui/ModifierKeys.qml
%{_datadir}/kpackage/kcms/kcm_access/contents/ui/MouseNavigation.qml
%{_datadir}/kpackage/kcms/kcm_access/contents/ui/ScreenReader.qml
%{_datadir}/kpackage/kcms/kcm_access/contents/ui/main.qml
%dir %{_datadir}/kpackage/kcms/kcm_tablet
%dir %{_datadir}/kpackage/kcms/kcm_tablet/contents
%dir %{_datadir}/kpackage/kcms/kcm_tablet/contents/ui
%{_datadir}/kpackage/kcms/kcm_tablet/contents/ui/main.qml
%{_datadir}/plasma/packages/org.kde.desktoptoolbox/contents/ui/ToolBoxContent.qml
%{_datadir}/qlogging-categories5/kcm_tablet.categories
%{_datadir}/qlogging-categories5/kcm_mouse.categories
%dir %{_datadir}/kcmmouse
%{_datadir}/kcmmouse/cursor*.pcf.gz
%{_datadir}/kcmmouse/pics
%{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.marginsseparator.so
%{_libdir}/qt5/plugins/plasma/kcms/desktop/kcm_krunnersettings.so
%{_desktopdir}/kcm_krunnersettings.desktop
%{_datadir}/config.kcfg/krunnersettingsbase.kcfg
%{_datadir}/config.kcfg/workspaceoptions_kwinsettings.kcfg
%{_datadir}/kpackage/kcms/kcm_krunnersettings/contents/ui/main.qml
