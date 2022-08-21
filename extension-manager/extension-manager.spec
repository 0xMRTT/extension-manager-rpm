Name:      extension-manager
Version:   0.3.1
Release:   %autorelease
Summary:   A utility for browsing and installing GNOME Shell Extensions. 
BuildArch: noarch
License:   GPL-3.0-or-later
URL:       https://github.com/mjakeman/extension-manager
Source0:   https://github.com/mjakeman/extension-manager/archive/refs/tags/v0.3.1.tar.gz

BuildRequires:  meson
BuildRequires:  blueprint-compiler
BuildRequires:  text-engine
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) 
BuildRequires:  libsoup3
BuildRequires:  json-glib

%build
%meson
%meson_build


%install
%meson_install
