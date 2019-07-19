#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-sisu-guice
Version  : 3.1.0
Release  : 3
URL      : https://repo1.maven.org/maven2/org/sonatype/sisu/sisu-guice/3.1.0/sisu-guice-3.1.0.jar
Source0  : https://repo1.maven.org/maven2/org/sonatype/sisu/sisu-guice/3.1.0/sisu-guice-3.1.0.jar
Source1  : https://repo.maven.apache.org/maven2/org/sonatype/sisu/sisu-guice/2.1.7/sisu-guice-2.1.7-noaop.jar
Source2  : https://repo1.maven.org/maven2/org/sonatype/sisu/sisu-guice/2.1.7/sisu-guice-2.1.7.jar
Source3  : https://repo1.maven.org/maven2/org/sonatype/sisu/sisu-guice/2.1.7/sisu-guice-2.1.7.pom
Source4  : https://repo1.maven.org/maven2/org/sonatype/sisu/sisu-guice/3.1.0/sisu-guice-3.1.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-sisu-guice-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-sisu-guice package.
Group: Data

%description data
data components for the mvn-sisu-guice package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/sisu/sisu-guice/3.1.0
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/sisu/sisu-guice/3.1.0/sisu-guice-3.1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/sisu/sisu-guice/2.1.7
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/sisu/sisu-guice/2.1.7/sisu-guice-2.1.7-noaop.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/sisu/sisu-guice/2.1.7
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/sisu/sisu-guice/2.1.7/sisu-guice-2.1.7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/sisu/sisu-guice/2.1.7
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/sisu/sisu-guice/2.1.7/sisu-guice-2.1.7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/sisu/sisu-guice/3.1.0
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/sisu/sisu-guice/3.1.0/sisu-guice-3.1.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/sonatype/sisu/sisu-guice/2.1.7/sisu-guice-2.1.7-noaop.jar
/usr/share/java/.m2/repository/org/sonatype/sisu/sisu-guice/2.1.7/sisu-guice-2.1.7.jar
/usr/share/java/.m2/repository/org/sonatype/sisu/sisu-guice/2.1.7/sisu-guice-2.1.7.pom
/usr/share/java/.m2/repository/org/sonatype/sisu/sisu-guice/3.1.0/sisu-guice-3.1.0.jar
/usr/share/java/.m2/repository/org/sonatype/sisu/sisu-guice/3.1.0/sisu-guice-3.1.0.pom
