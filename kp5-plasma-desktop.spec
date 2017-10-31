# TODO:
# PackageKit qt5
#
%define		kdeplasmaver	5.11.2
%define		qtver		5.3.2
%define		kpname		plasma-desktop

Summary:	KDE Plasma Desktop
Name:		kp5-%{kpname}
Version:	5.11.2
Release:	2
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	b9d8aa7f4e94fba10a47d0b4768c1029
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	fontconfig-devel
BuildRequires:	kf5-attica-devel
BuildRequires:	kf5-kactivities-stats-devel
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
BuildRequires:	kp5-breeze-devel
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
/etc/dbus-1/system.d/org.kde.fontinst.conf
/etc/dbus-1/system.d/org.kde.kcontrol.kcmclock.conf
/etc/xdg/colorschemes.knsrc
/etc/xdg/emoticons.knsrc
/etc/xdg/icons.knsrc
/etc/xdg/kfontinst.knsrc
/etc/xdg/lookandfeel.knsrc
/etc/xdg/plasma-themes.knsrc
/etc/xdg/xcursor.knsrc
%attr(755,root,root) %{_bindir}/kaccess
%attr(755,root,root) %{_bindir}/kapplymousetheme
%attr(755,root,root) %{_bindir}/kcm-touchpad-list-devices
%attr(755,root,root) %{_bindir}/kcolorschemeeditor
%attr(755,root,root) %{_bindir}/kfontinst
%attr(755,root,root) %{_bindir}/kfontview
%attr(755,root,root) %{_bindir}/knetattach
%attr(755,root,root) %{_bindir}/krdb
%attr(755,root,root) %{_bindir}/solid-action-desktop-gen
%{_libdir}/kauth/fontinst
%{_libdir}/kauth/fontinst_helper
%{_libdir}/kauth/fontinst_x11
%{_libdir}/kauth/kcmdatetimehelper
%{_libdir}/kconf_update_bin/krdb_clearlibrarypath
%{_libdir}/kfontprint
%{_libdir}/kimpanel-ibus-panel
%{_libdir}/kimpanel-ibus-panel-launcher
%{_libdir}/kimpanel-scim-panel
%{_libdir}/libkdeinit5_kaccess.so
%{_libdir}/libkfontinst.so
%{_libdir}/libkfontinst.so.5
%{_libdir}/libkfontinst.so.5.*.*
%{_libdir}/libkfontinstui.so
%{_libdir}/libkfontinstui.so.5
%{_libdir}/libkfontinstui.so.5.*.*
%{_libdir}/plasma-changeicons
%{_libdir}/qt5/plugins/attica_kde.so
%{_libdir}/qt5/plugins/fontthumbnail.so
%{_libdir}/qt5/plugins/kcm_access.so
%{_libdir}/qt5/plugins/kcm_activities.so
%{_libdir}/qt5/plugins/kcm_autostart.so
%{_libdir}/qt5/plugins/kcm_baloofile.so
%{_libdir}/qt5/plugins/kcm_clock.so
%{_libdir}/qt5/plugins/kcm_colors.so
%{_libdir}/qt5/plugins/kcm_componentchooser.so
%{_libdir}/qt5/plugins/kcm_cursortheme.so
%{_libdir}/qt5/plugins/kcm_desktoppaths.so
%{_libdir}/qt5/plugins/kcm_emoticons.so
%{_libdir}/qt5/plugins/kcm_fontinst.so
%{_libdir}/qt5/plugins/kcm_fonts.so
%{_libdir}/qt5/plugins/kcm_formats.so
%{_libdir}/qt5/plugins/kcm_icons.so
%{_libdir}/qt5/plugins/kcm_input.so
%{_libdir}/qt5/plugins/kcm_joystick.so
%{_libdir}/qt5/plugins/kcm_kded.so
%{_libdir}/qt5/plugins/kcm_keyboard.so
%{_libdir}/qt5/plugins/kcm_keys.so
%{_libdir}/qt5/plugins/kcm_knotify.so
%{_libdir}/qt5/plugins/kcm_launch.so
%{_libdir}/qt5/plugins/kcm_phonon.so
%{_libdir}/qt5/plugins/kcm_plasmasearch.so
%{_libdir}/qt5/plugins/kcm_smserver.so
%{_libdir}/qt5/plugins/kcm_solid_actions.so
%{_libdir}/qt5/plugins/kcm_standard_actions.so
%{_libdir}/qt5/plugins/kcm_style.so
%{_libdir}/qt5/plugins/kcm_workspaceoptions.so
%dir %{_libdir}/qt5/plugins/kcms
%{_libdir}/qt5/plugins/kcms/kcm_desktoptheme.so
%{_libdir}/qt5/plugins/kcms/kcm_lookandfeel.so
%{_libdir}/qt5/plugins/kcms/kcm_splashscreen.so
%{_libdir}/qt5/plugins/kcmspellchecking.so
%{_libdir}/qt5/plugins/kded_touchpad.so
%{_libdir}/qt5/plugins/kf5/kded/device_automounter.so
%{_libdir}/qt5/plugins/kf5/kded/keyboard.so
%{_libdir}/qt5/plugins/kfontviewpart.so
%{_libdir}/qt5/plugins/kio_fonts.so
%{_libdir}/qt5/plugins/krunner_kwin.so
%{_libdir}/qt5/plugins/krunner_plasma-desktop.so
%{_libdir}/qt5/plugins/libkcm_device_automounter.so
%{_libdir}/qt5/plugins/libkcm_translations.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_kimpanel.so
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_touchpad.so
%dir %{_libdir}/qt5/qml/org/kde/activities/settings
%{_libdir}/qt5/qml/org/kde/activities/settings/libkactivitiessettingsplugin.so
%{_libdir}/qt5/qml/org/kde/activities/settings/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/activityswitcher
%{_libdir}/qt5/qml/org/kde/plasma/activityswitcher/libactivityswitcherextensionplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/activityswitcher/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/kicker
%{_libdir}/qt5/qml/org/kde/plasma/private/kicker/libkickerplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/kicker/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/kimpanel
%{_libdir}/qt5/qml/org/kde/plasma/private/kimpanel/libkimpanelplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/kimpanel/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/pager
%{_libdir}/qt5/qml/org/kde/plasma/private/pager/libpagerplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/pager/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/taskmanager
%{_libdir}/qt5/qml/org/kde/plasma/private/taskmanager/libtaskmanagerplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/taskmanager/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/trash
%{_libdir}/qt5/qml/org/kde/plasma/private/trash/libtrashplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/trash/qmldir
%dir %{_libdir}/qt5/qml/org/kde/private/desktopcontainment/
%dir %{_libdir}/qt5/qml/org/kde/private/desktopcontainment/desktop
%{_libdir}/qt5/qml/org/kde/private/desktopcontainment/desktop/libdesktopplugin.so
%{_libdir}/qt5/qml/org/kde/private/desktopcontainment/desktop/qmldir
%dir %{_libdir}/qt5/qml/org/kde/private/desktopcontainment/folder
%{_libdir}/qt5/qml/org/kde/private/desktopcontainment/folder/libfolderplugin.so
%{_libdir}/qt5/qml/org/kde/private/desktopcontainment/folder/qmldir
%{_desktopdir}/org.kde.kcolorschemeeditor.desktop
%{_desktopdir}/org.kde.kfontview.desktop
%{_desktopdir}/org.kde.knetattach.desktop
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
%{_iconsdir}/hicolor/128x128/devices/input-touchpad.png
%{_iconsdir}/hicolor/128x128/mimetypes/fonts-package.png
%{_iconsdir}/hicolor/16x16/apps/kfontview.png
%{_iconsdir}/hicolor/16x16/devices/input-touchpad.png
%{_iconsdir}/hicolor/16x16/mimetypes/fonts-package.png
%{_iconsdir}/hicolor/22x22/apps/kfontview.png
%{_iconsdir}/hicolor/22x22/devices/input-touchpad.png
%{_iconsdir}/hicolor/22x22/mimetypes/fonts-package.png
%{_iconsdir}/hicolor/24x24/devices/input-touchpad.png
%{_iconsdir}/hicolor/256x256/devices/input-touchpad.png
%{_iconsdir}/hicolor/32x32/apps/kfontview.png
%{_iconsdir}/hicolor/32x32/devices/input-touchpad.png
%{_iconsdir}/hicolor/32x32/mimetypes/fonts-package.png
%{_iconsdir}/hicolor/48x48/apps/kfontview.png
%{_iconsdir}/hicolor/48x48/devices/input-touchpad.png
%{_iconsdir}/hicolor/48x48/mimetypes/fonts-package.png
%{_iconsdir}/hicolor/64x64/apps/kfontview.png
%{_iconsdir}/hicolor/64x64/devices/input-touchpad.png
%{_iconsdir}/hicolor/64x64/mimetypes/fonts-package.png
%{_iconsdir}/hicolor/96x96/devices/input-touchpad.png
%{_iconsdir}/hicolor/scalable/apps/preferences-desktop-font-installer.svgz
%{_iconsdir}/hicolor/scalable/devices/input-touchpad.svgz
%dir %{_datadir}/kcm_componentchooser
%{_datadir}/kcm_componentchooser/kcm_browser.desktop
%{_datadir}/kcm_componentchooser/kcm_filemanager.desktop
%{_datadir}/kcm_componentchooser/kcm_kemail.desktop
%{_datadir}/kcm_componentchooser/kcm_terminal.desktop
%dir %{_datadir}/kcm_phonon
%{_datadir}/kcm_phonon/listview-background.png
%dir %{_datadir}/kcminput
%{_datadir}/kcminput/cursor_large_black.pcf.gz
%{_datadir}/kcminput/cursor_large_white.pcf.gz
%{_datadir}/kcminput/cursor_small_white.pcf.gz
%dir %{_datadir}/kcminput/pics
%{_datadir}/kcminput/pics/mouse_lh.png
%{_datadir}/kcminput/pics/mouse_rh.png
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
%{_datadir}/kconf_update/krdb_libpathwipe.upd
%dir %{_datadir}/kcontrol
%dir %{_datadir}/kcontrol/pics
%{_datadir}/kcontrol/pics/logo.png
%{_datadir}/kcontrol/pics/mini-world.png
%dir %{_datadir}/kdisplay
%dir %{_datadir}/kdisplay/app-defaults
%{_datadir}/kdisplay/app-defaults/AAAAAAGeneral.ad
%{_datadir}/kdisplay/app-defaults/AAAMotif.ad
%{_datadir}/kdisplay/app-defaults/AAATk.ad
%{_datadir}/kdisplay/app-defaults/AAAXaw.ad
%{_datadir}/kdisplay/app-defaults/AcroRead.ad
%{_datadir}/kdisplay/app-defaults/Editres.ad
%{_datadir}/kdisplay/app-defaults/Emacs.ad
%{_datadir}/kdisplay/app-defaults/GV.ad
%{_datadir}/kdisplay/app-defaults/ML.ad
%{_datadir}/kdisplay/app-defaults/Nedit.ad
%{_datadir}/kdisplay/app-defaults/Netscape.ad
%{_datadir}/kdisplay/app-defaults/RVPlayer.ad
%{_datadir}/kdisplay/app-defaults/WPerfect.ad
%{_datadir}/kdisplay/app-defaults/XCalc.ad
%{_datadir}/kdisplay/app-defaults/XOsview.ad
%{_datadir}/kdisplay/app-defaults/XTerm.ad
%{_datadir}/kdisplay/app-defaults/XV.ad
%{_datadir}/kdisplay/app-defaults/Xawtv.ad
%{_datadir}/kdisplay/app-defaults/Xdvi.ad
%{_datadir}/kdisplay/app-defaults/Xpdf.ad
%dir %{_datadir}/kf5/kactivitymanagerd
%dir %{_datadir}/kf5/kactivitymanagerd/workspace
%dir %{_datadir}/kf5/kactivitymanagerd/workspace/settings
%dir %{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml
%dir %{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activitiesTab
%{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activitiesTab/ActivitiesView.qml
%{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activitiesTab/main.qml
%dir %{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activityDialog
%{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activityDialog/GeneralTab.qml
%{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activityDialog/OtherTab.qml
%dir %{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activityDialog/components
%{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activityDialog/components/DialogButtons.qml
%{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activityDialog/components/IconChooser.qml
%{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activityDialog/components/LabeledTextField.qml
%{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/activityDialog/components/ShortcutChooser.qml
%dir %{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/privacyTab
%{_datadir}/kf5/kactivitymanagerd/workspace/settings/qml/privacyTab/BlacklistApplicationView.qml
%dir %{_datadir}/kfontinst
%dir %{_datadir}/kfontinst/icons
%dir %{_datadir}/kfontinst/icons/hicolor
%dir %{_datadir}/kfontinst/icons/hicolor/16x16
%dir %{_datadir}/kfontinst/icons/hicolor/16x16/actions
%{_datadir}/kfontinst/icons/hicolor/16x16/actions/addfont.png
%{_datadir}/kfontinst/icons/hicolor/16x16/actions/disablefont.png
%{_datadir}/kfontinst/icons/hicolor/16x16/actions/enablefont.png
%{_datadir}/kfontinst/icons/hicolor/16x16/actions/fontstatus.png
%dir %{_datadir}/kfontinst/icons/hicolor/22x22
%dir %{_datadir}/kfontinst/icons/hicolor/22x22/actions
%{_datadir}/kfontinst/icons/hicolor/22x22/actions/addfont.png
%{_datadir}/kfontinst/icons/hicolor/22x22/actions/disablefont.png
%{_datadir}/kfontinst/icons/hicolor/22x22/actions/enablefont.png
%{_datadir}/kfontinst/icons/hicolor/22x22/actions/fontstatus.png
%{_datadir}/knotifications5/kaccess.notifyrc
%{_datadir}/knotifications5/kcm_touchpad.notifyrc
%dir %{_datadir}/konqsidebartng
%dir %{_datadir}/konqsidebartng/virtual_folders
%dir %{_datadir}/konqsidebartng/virtual_folders/services
%{_datadir}/konqsidebartng/virtual_folders/services/fonts.desktop
%dir %{_datadir}/kpackage/kcms
%dir %{_datadir}/kpackage/kcms/kcm_desktoptheme
%dir %{_datadir}/kpackage/kcms/kcm_desktoptheme/contents
%dir %{_datadir}/kpackage/kcms/kcm_desktoptheme/contents/ui
%{_datadir}/kpackage/kcms/kcm_desktoptheme/contents/ui/Hand.qml
%{_datadir}/kpackage/kcms/kcm_desktoptheme/contents/ui/ThemePreview.qml
%{_datadir}/kpackage/kcms/kcm_desktoptheme/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_desktoptheme/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_desktoptheme/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_lookandfeel
%dir %{_datadir}/kpackage/kcms/kcm_lookandfeel/contents
%dir %{_datadir}/kpackage/kcms/kcm_lookandfeel/contents/ui
%{_datadir}/kpackage/kcms/kcm_lookandfeel/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_lookandfeel/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_lookandfeel/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_splashscreen
%dir %{_datadir}/kpackage/kcms/kcm_splashscreen/contents
%dir %{_datadir}/kpackage/kcms/kcm_splashscreen/contents/ui
%{_datadir}/kpackage/kcms/kcm_splashscreen/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_splashscreen/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_splashscreen/metadata.json
%{_datadir}/kservices5/ServiceMenus/installfont.desktop
%{_datadir}/kservices5/autostart.desktop
%{_datadir}/kservices5/clock.desktop
%{_datadir}/kservices5/colors.desktop
%{_datadir}/kservices5/componentchooser.desktop
%{_datadir}/kservices5/cursortheme.desktop
%{_datadir}/kservices5/desktoppath.desktop
%{_datadir}/kservices5/device_automounter_kcm.desktop
%{_datadir}/kservices5/emoticons.desktop
%{_datadir}/kservices5/fontinst.desktop
%{_datadir}/kservices5/fonts.desktop
%{_datadir}/kservices5/fonts.protocol
%{_datadir}/kservices5/fontthumbnail.desktop
%{_datadir}/kservices5/formats.desktop
%{_datadir}/kservices5/icons.desktop
%{_datadir}/kservices5/joystick.desktop
%{_datadir}/kservices5/kaccess.desktop
%{_datadir}/kservices5/kcm_activities.desktop
%{_datadir}/kservices5/kcm_baloofile.desktop
%{_datadir}/kservices5/kcm_desktoptheme.desktop
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
%{_datadir}/kservices5/kded/touchpad.desktop
%{_datadir}/kservices5/keys.desktop
%{_datadir}/kservices5/kfontviewpart.desktop
%{_datadir}/kservices5/mouse.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.icontasks.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.kicker.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.kickoff.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.kimpanel.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.pager.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.showActivityManager.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.taskmanager.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.trash.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.windowlist.desktop
%{_datadir}/kservices5/plasma-applet-touchpad.desktop
%{_datadir}/kservices5/plasma-containment-org.kde.desktopcontainment.desktop
%{_datadir}/kservices5/plasma-containment-org.kde.panel.desktop
%{_datadir}/kservices5/plasma-containment-org.kde.plasma.folder.desktop
%{_datadir}/kservices5/plasma-dataengine-kimpanel.desktop
%{_datadir}/kservices5/plasma-dataengine-touchpad.desktop
%{_datadir}/kservices5/plasma-layout-template-org.kde.plasma.desktop.appmenubar.desktop
%{_datadir}/kservices5/plasma-layout-template-org.kde.plasma.desktop.defaultPanel.desktop
%{_datadir}/kservices5/plasma-layout-template-org.kde.plasma.desktop.emptyPanel.desktop
%{_datadir}/kservices5/plasma-package-org.kde.desktoptoolbox.desktop
%{_datadir}/kservices5/plasma-package-org.kde.paneltoolbox.desktop
%{_datadir}/kservices5/plasma-runner-kwin.desktop
%{_datadir}/kservices5/plasma-runner-plasma-desktop.desktop
%{_datadir}/kservices5/plasma-shell-org.kde.plasma.desktop.desktop
%{_datadir}/kservices5/solid-actions.desktop
%{_datadir}/kservices5/spellchecking.desktop
%{_datadir}/kservices5/standard_actions.desktop
%{_datadir}/kservices5/style.desktop
%{_datadir}/kservices5/translations.desktop
%{_datadir}/kservices5/workspaceoptions.desktop
%{_datadir}/kservicetypes5/solid-device-type.desktop
%dir %{_datadir}/kxmlgui5/kfontinst
%{_datadir}/kxmlgui5/kfontinst/kfontviewpart.rc
%dir %{_datadir}/kxmlgui5/kfontview
%{_datadir}/kxmlgui5/kfontview/kfontviewui.rc
%{_datadir}/metainfo/org.kde.desktopcontainment.appdata.xml
%{_datadir}/metainfo/org.kde.desktoptoolbox.appdata.xml
%{_datadir}/metainfo/org.kde.paneltoolbox.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.desktop.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.desktop.appmenubar.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.desktop.defaultPanel.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.desktop.emptyPanel.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.folder.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.icontasks.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.kicker.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.kickoff.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.kimpanel.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.pager.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.showActivityManager.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.taskmanager.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.trash.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.windowlist.appdata.xml
%{_datadir}/metainfo/org.kde.plasmashell.metainfo.xml
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
%{_datadir}/plasma/packages/org.kde.desktoptoolbox/contents/config/main.xml
%dir %{_datadir}/plasma/packages/org.kde.desktoptoolbox/contents/ui
%{_datadir}/plasma/packages/org.kde.desktoptoolbox/contents/ui/ToolBoxButton.qml
%{_datadir}/plasma/packages/org.kde.desktoptoolbox/contents/ui/ToolBoxItem.qml
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
%dir %{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/code
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/code/FolderTools.js
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/code/LayoutManager.js
%dir %{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/config
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/ActionButton.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/AppletAppearance.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/AppletHandle.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/BackButtonItem.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/BusyOverlay.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/CompactRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/ConfigFilter.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/ConfigIcons.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/ConfigLocation.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/ConfigTweaks.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/FolderItemActionButton.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/FolderItemDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/FolderItemPreviewPluginsDialog.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/FolderView.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/FolderViewDialog.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/FolderViewDropArea.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/FolderViewLayer.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/ResizeHandle.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.desktopcontainment/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.panel
%dir %{_datadir}/plasma/plasmoids/org.kde.panel/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.panel/contents/code
%{_datadir}/plasma/plasmoids/org.kde.panel/contents/code/LayoutManager.js
%dir %{_datadir}/plasma/plasmoids/org.kde.panel/contents/config
%{_datadir}/plasma/plasmoids/org.kde.panel/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.panel/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.panel/contents/ui/ConfigOverlay.qml
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
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kicker
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/code
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/code/tools.js
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/ui
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
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.kicker/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/code
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/code/tools.js
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/ActionMenu.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/ApplicationsView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/BaseView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/Breadcrumb.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/ComputerView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/ConfigButtons.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/ConfigGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/FavoritesView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/Footer.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/FullRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/Header.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/Kickoff.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/KickoffButton.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/KickoffConfigurationButton.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/KickoffHighlight.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/KickoffItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/LeaveView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/OftenUsedView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/RecentlyUsedView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/SearchView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/SectionDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickoff/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents/ui/ActionMenu.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents/ui/ConfigAppearance.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents/ui/ContextMenu.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents/ui/InputPanel.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents/ui/StatusIcon.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/metadata.json
#%%{_datadir}/plasma/plasmoids/org.kde.plasma.pager/contents/code/utils.js
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.pager
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.pager/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.pager/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.pager/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.pager/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.pager/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.pager/contents/ui/configGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.pager/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.pager/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.pager/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.showActivityManager
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.showActivityManager/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.showActivityManager/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.showActivityManager/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.showActivityManager/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.showActivityManager/metadata.json
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/code
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/code/layout.js
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/code/tools.js
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/AudioStream.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/ConfigGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/ContextMenu.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/GroupDialog.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/GroupExpanderOverlay.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/MouseHandler.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/PulseAudio.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/Task.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/TaskBadgeOverlay.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/TaskList.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/TaskProgressOverlay.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/ToolTipDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/ToolTipInstance.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.taskmanager/contents/ui/ToolTipWindowMouseArea.qml
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
%{_datadir}/plasma/services/kimpanel.operations
%{_datadir}/plasma/services/touchpad.operations
%dir %{_datadir}/plasma/shells/org.kde.plasma.desktop
%dir %{_datadir}/plasma/shells/org.kde.plasma.desktop/contents
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/InteractiveConsole.qml
%dir %{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/activitymanager
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/activitymanager/ActivityItem.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/activitymanager/ActivityList.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/activitymanager/ActivityManager.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/activitymanager/Heading.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/activitymanager/StoppedActivityItem.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/activitymanager/WindowPreview.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/activitymanager/static.js
%dir %{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/applet
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/applet/AppletError.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/applet/CompactApplet.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/applet/DefaultCompactRepresentation.qml
%dir %{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration/AppletConfiguration.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration/ConfigCategoryDelegate.qml
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
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration/panelconfiguration/SizeHandle.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration/panelconfiguration/SliderHandle.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/configuration/panelconfiguration/ToolBar.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/defaults
%dir %{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/explorer
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/explorer/AppletAlternatives.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/explorer/AppletDelegate.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/explorer/Tooltip.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/explorer/WidgetExplorer.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/layout.js
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/loader.qml
%dir %{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/updates
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/updates/obsolete_kickoffrc.js
%dir %{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/views
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/views/Desktop.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/contents/views/Panel.qml
%{_datadir}/plasma/shells/org.kde.plasma.desktop/metadata.desktop
%{_datadir}/plasma/shells/org.kde.plasma.desktop/metadata.json
%{_datadir}/polkit-1/actions/org.kde.fontinst.policy
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmclock.policy
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
%{_datadir}/plasma/plasmoids/org.kde.plasma.kimpanel/contents/ui/CandidateHighlight.qml
