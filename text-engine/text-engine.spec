
%global         forgeurl https://github.com/mjakeman/text-engine

Name:           text-engine
Version:        0.1.1
Release:        %autorelease
Summary:        A lightweight rich text framework for GTK

%forgemeta

License:        LGPL-2.1-or-later
URL:            https://github.com/mjakeman/text-engine/
Source0:        %{forgesource}

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0) 
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50

%description
Text Engine is a rich-text editing framework for GTK 4. The primary user of this library is bluetype but it can be used wherever rich text display and editing is needed.


%prep
%forgeautosetup


%build
%meson
%meson_build


%install
%meson_install

%files
%license COPYING 
%doc README.md
%{_libdir}/text-engine/*
# add others files

%changelog
%autochangelog
