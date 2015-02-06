Name:		xtux
Version:	20030306
Release:	14
Summary:	Multiplayer arcade game featuring open-source mascots
Group:		Games/Arcade
License:	GPL+ and LGPLv2+
URL:		http://xtux.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.tar.bz2
Source1:	%{name}-16.png
Source2:	%{name}-32.png
Source3:	%{name}-48.png
Patch:		xtux-fix-format-strings.patch
BuildRequires:	xpm-devel

%description
2005: Microsoft finally releases Windows2000. The few remaining in line
from midnight December 31, 1999 expecting Microsoft to deliver "on time"
were slightly annoyed, but otherwise the response was extremely
enthusiastic.

...

You must Battle through hoards of Evil Microsoft lusers, Certified Peons
and Bugs while collecting computer processors. Using these, construct a
massive Beowulf machine capable of cracking the security on Microsofts
secret database. Upload yourself into the internet, liberate friendly
Linux sites, then battle your way into microsoft.com destroying all you
can find. Only then can you turn your wrath towards your nemisis, the
evil lord Gates.

%prep
%setup -q -n %{name}
%patch -p2
%{__perl} -pi -e 's|./tux_serv|%{_gamesbindir}/tux_serv|;' src/client/menu.c

%build
%{make} CC="%{__cc} %{optflags}" DATADIR="%{_gamesdatadir}/%{name}" X11LIB="-lX11"

%install
%{__mkdir_p} %{buildroot}%{_gamesbindir}
%{__install} -m 755 %{name} %{buildroot}%{_gamesbindir}
%{__mkdir_p} %{buildroot}%{_sbindir}
%{__install} -m 755 tux_serv %{buildroot}%{_gamesbindir}

%{__mkdir_p} %{buildroot}%{_gamesdatadir}/%{name}
cp -a data/* %{buildroot}%{_gamesdatadir}/%{name}

# icons
%{__install} -D -m 644 %{SOURCE1} %{buildroot}%{_liconsdir}/%{name}.png
%{__install} -D -m 644 %{SOURCE2} %{buildroot}%{_iconsdir}/%{name}.png
%{__install} -D -m 644 %{SOURCE3} %{buildroot}%{_miconsdir}/%{name}.png

# menus

%{__mkdir_p} %{buildroot}%{_datadir}/applications
%{__cat} > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=X-Tux
Comment=X-Tux
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

%{_bindir}/find %{buildroot}%{_gamesdatadir}/%{name}/images -type d -name ".xvpics" | %{_bindir}/xargs -t %{__rm} -r

%files
%defattr(0644,root,root,0755)
%doc AUTHORS CHANGELOG COPYING README README.GGZ doc/*
%attr(0755,root,root) %{_gamesbindir}/%{name}
%attr(0755,root,root) %{_gamesbindir}/tux_serv
%{_gamesdatadir}/%{name}
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/*

