Name:           mediainfo
Version:        0.7.56
Release:        1%{?dist}
Summary:        Supplies technical and tag information about a video or audio file (CLI)
Summary(ru):    Предоставляет полную информацию о медиа файле (CLI)

License:        GPL
Group:          Applications/Multimedia
URL:            http://mediainfo.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}_%{version}.tar.bz2
Source100:      README.RFRemix

BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  libmediainfo-devel >= %{version}
BuildRequires:  libzen-devel >= 0.4.26
BuildRequires:  pkgconfig
BuildRequires:  wxGTK-devel
BuildRequires:  zlib-devel
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  autoconf

%description
MediaInfo CLI (Command Line Interface).

What information can I get from MediaInfo?
* General: title, author, director, album, track number, date, duration...
* Video: codec, aspect, fps, bitrate...
* Audio: codec, sample rate, channels, language, bitrate...
* Text: language of subtitle
* Chapters: number of chapters, list of chapters

DivX, XviD, H263, H.263, H264, x264, ASP, AVC, iTunes, MPEG-1,
MPEG1, MPEG-2, MPEG2, MPEG-4, MPEG4, MP4, M4A, M4V, QuickTime,
RealVideo, RealAudio, RA, RM, MSMPEG4v1, MSMPEG4v2, MSMPEG4v3,
VOB, DVD, WMA, VMW, ASF, 3GP, 3GPP, 3GP2

What format (container) does MediaInfo support?
* Video: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1,
  MPEG-2, MPEG-4, DVD (VOB) (Codecs: DivX, XviD, MSMPEG4, ASP,
  H.264, AVC...)
* Audio: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF
* Subtitles: SRT, SSA, ASS, SAMI

%description -l ru
MediaInfo CLI (интерфейс командной строки).

Какая информация может быть получена MediaInfo?
* Общее: title, author, director, album, track number, date, duration...
* Видео: codec, aspect, fps, bitrate...
* Аудио: codec, sample rate, channels, language, bitrate...
* Текст: язык субтитров
* Части: число частей, список частей

DivX, XviD, H263, H.263, H264, x264, ASP, AVC, iTunes, MPEG-1,
MPEG1, MPEG-2, MPEG2, MPEG-4, MPEG4, MP4, M4A, M4V, QuickTime,
RealVideo, RealAudio, RA, RM, MSMPEG4v1, MSMPEG4v2, MSMPEG4v3,
VOB, DVD, WMA, VMW, ASF, 3GP, 3GPP, 3GP2

Какой формат (контейнер) поддерживает MediaInfo?
* Видео: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1,
  MPEG-2, MPEG-4, DVD (VOB) (Codecs: DivX, XviD, MSMPEG4, ASP,
  H.264, AVC...)
* Аудио: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF
* Субтитры: SRT, SSA, ASS, SAMI

%package gui
Summary:    Supplies technical and tag information about a video or audio file (GUI)
Summary(ru):Предоставляет полную информацию о медиа файле (GUI)
Group:      Applications/Multimedia
Requires:   libzen >= 0.4.26
Requires:   libmediainfo >= %{version}

%description gui
MediaInfo (Graphical User Interface).

What information can I get from MediaInfo?
* General: title, author, director, album, track number, date, duration...
* Video: codec, aspect, fps, bitrate...
* Audio: codec, sample rate, channels, language, bitrate...
* Text: language of subtitle
* Chapters: number of chapters, list of chapters

DivX, XviD, H263, H.263, H264, x264, ASP, AVC, iTunes, MPEG-1,
MPEG1, MPEG-2, MPEG2, MPEG-4, MPEG4, MP4, M4A, M4V, QuickTime,
RealVideo, RealAudio, RA, RM, MSMPEG4v1, MSMPEG4v2, MSMPEG4v3,
VOB, DVD, WMA, VMW, ASF, 3GP, 3GPP, 3GP2

What format (container) does MediaInfo support?
* Video: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1,
  MPEG-2, MPEG-4, DVD (VOB) (Codecs: DivX, XviD, MSMPEG4, ASP,
  H.264, AVC...)
* Audio: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF
* Subtitles: SRT, SSA, ASS, SAMI

%description gui -l ru
MediaInfo (графический интерфейс пользователя).

Какая информация может быть получена MediaInfo?
* Общее: title, author, director, album, track number, date, duration...
* Видео: codec, aspect, fps, bitrate...
* Аудио: codec, sample rate, channels, language, bitrate...
* Текст: язык субтитров
* Части: число частей, список частей

DivX, XviD, H263, H.263, H264, x264, ASP, AVC, iTunes, MPEG-1,
MPEG1, MPEG-2, MPEG2, MPEG-4, MPEG4, MP4, M4A, M4V, QuickTime,
RealVideo, RealAudio, RA, RM, MSMPEG4v1, MSMPEG4v2, MSMPEG4v3,
VOB, DVD, WMA, VMW, ASF, 3GP, 3GPP, 3GP2

Какой формат (контейнер) поддерживает MediaInfo?
* Видео: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1,
  MPEG-2, MPEG-4, DVD (VOB) (Codecs: DivX, XviD, MSMPEG4, ASP,
  H.264, AVC...)
* Аудио: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF
* Субтитры: SRT, SSA, ASS, SAMI

%prep
%setup -q -n MediaInfo
dos2unix     *.html *.txt Release/*.txt
%__chmod 644 *.html *.txt Release/*.txt

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"

# build CLI
pushd Project/GNU/CLI
    %__chmod +x autogen
    ./autogen
    %configure

    %__make %{?jobs:-j%{jobs}}
popd

# now build GUI
pushd Project/GNU/GUI
    %__chmod +x autogen
    ./autogen
    %configure

    %__make %{?jobs:-j%{jobs}}
popd

cp %{SOURCE100} .

%install
pushd Project/GNU/CLI
    %__make install-strip DESTDIR=%{buildroot}
popd

pushd Project/GNU/GUI
    %__make install-strip DESTDIR=%{buildroot}
popd

# icon
%__install -dm 755 %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
%__install -m 644 Source/Resource/Image/MediaInfo.png \
    %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%__install -dm 755 %{buildroot}%{_datadir}/pixmaps
%__install -m 644 Source/Resource/Image/MediaInfo.png \
    %{buildroot}%{_datadir}/pixmaps/%{name}.png

# menu-entry
%__install -dm 755 %{buildroot}/%{_datadir}/applications
%__install -m 644 Project/GNU/GUI/mediainfo-gui.desktop \
    %{buildroot}/%{_datadir}/applications
%__install -dm 755 %{buildroot}/%{_datadir}/apps/konqueror/servicemenus
%__install -m 644 Project/GNU/GUI/mediainfo-gui.kde3.desktop \
    %{buildroot}/%{_datadir}/apps/konqueror/servicemenus/mediainfo-gui.desktop
%__install -dm 755 %{buildroot}/%{_datadir}/kde4/services/ServiceMenus/
%__install -m 644 Project/GNU/GUI/mediainfo-gui.kde4.desktop \
    %{buildroot}/%{_datadir}/kde4/services/ServiceMenus/mediainfo-gui.desktop

%clean
[ -d "%{buildroot}" -a "%{buildroot}" != "" ] && %__rm -rf "%{buildroot}"

%files
%defattr(-,root,root,-)
%doc Release/ReadMe_CLI_Linux.txt
%doc License.html History_CLI.txt
%doc README.RFRemix
%{_bindir}/mediainfo

%files gui
%defattr(-,root,root,-)
%doc Release/ReadMe_GUI_Linux.txt
%doc License.html History_GUI.txt
%{_bindir}/mediainfo-gui
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor/128x128/apps
%{_datadir}/icons/hicolor/128x128/apps/*.png
%dir %{_datadir}/apps
%dir %{_datadir}/apps/konqueror
%dir %{_datadir}/apps/konqueror/servicemenus
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%dir %{_datadir}/kde4
%dir %{_datadir}/kde4/services
%dir %{_datadir}/kde4/services/ServiceMenus
%{_datadir}/kde4/services/ServiceMenus/*.desktop


%changelog
* Wed Apr 11 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.56-1.R
- Update to 0.7.56

* Tue Mar 20 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.54-1.R
- Update to 0.7.54

* Thu Feb 09 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.53-1.R
- Update to 0.7.53

* Thu Dec 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.52-1.R
- Update to 0.7.52

* Tue Nov 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.51-2.R
- Added description in russian language

* Mon Nov 14 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.51-1.R
- Update to 0.7.51

* Tue Sep 27 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.50-1.R
- Update to 0.7.50

* Mon Sep 19 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.49-1.R
- Update to 0.7.49

* Fri Aug 19 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.48-1.R
- Update to 0.7.48

* Tue Aug 09 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.47-2.R
- Removed 0 from name

* Thu Aug 05 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.47-1.R
- Initial release
