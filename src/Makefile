#Brief: Makefile for IVS project
#Project: Calculator
#File: Makefile
#File Author/s: Stanislav Gabriš <xgabri18(at)fit.vutbr.cz>
#Project Authors: Stanislav Gabriš <xgabri18(at)fit.vutbr.cz>
#				  Roman Országh <xorsza01(at)fit.vutbr.cz>
#				  Jarolím Antonín <xjarol06(at)fit.vutbr.cz>
#				  Vlk Jakub <xvlkja07(at)fit.vutbr.cz>
#######################################
#
#ZIP, MAKE, DOXYGEN, Python3.9 with pyinstaller, INNO SETUP for Windows used
#

AUTHORS=xorsza01_xgabri18_xvlkja07_xjarol06
PROJECT=calculator


TURNINDIR=turnin
REPODIR=repo
INSTALLDIR=install
DOCDIR=doc
TOSERVER=toSERVER
TOSERVERDIRS=$(DOCDIR) $(INSTALLDIR) $(REPODIR)
TOIS=toIS
TOEXCLUDE=.idea __pycache__ odevzdani.txt $(TURNINDIR) #directories which will not be submitted

#installer build
PYINSTIGNORE=build
PYINSTOK=dist
PYASSETS=assets
WHEREEXE=$(PYINSTOK)\calculator
WHEREINSTALLSCRIPT=installerscript
INSTALLERSCRIPT=innocalcscript.iss
WHEREINSTALLER=$(WHEREINSTALLSCRIPT)\Output




#Executes calculator.py
all:
	@echo Python program is not supposed to be built!
	@echo Running calculator.py instead...
	py -3 $(PROJECT).py

#Prepares compressed folders to be submitted
pack: toserver tois docu instal
	-cd .\$(TURNINDIR)\$(TOSERVER) & zip -r .\$(AUTHORS).zip .\$(AUTHORS) & del .\$(AUTHORS) /f /s /q & rmdir /s /q .\$(AUTHORS)
	cd .\$(TURNINDIR)\$(TOIS) & zip -r .\$(AUTHORS).zip .\$(AUTHORS) & del .\$(AUTHORS) /f /s /q & rmdir /s /q .\$(AUTHORS)
toserver:
	if exist ".\$(TURNINDIR)" del .\$(TURNINDIR) /f /s /q & rmdir /s /q .\$(TURNINDIR)
	md $(TURNINDIR)
	cd .\$(TURNINDIR) & md $(TOSERVER) & cd .\$(TOSERVER) & md $(AUTHORS) & cd .\$(AUTHORS) & md $(TOSERVERDIRS)
	-robocopy .. .\$(TURNINDIR)\$(TOSERVER)\$(AUTHORS)\$(REPODIR) /E /ZB /Z /XD $(TOEXCLUDE)
tois:
	cd .\$(TURNINDIR) & md $(TOIS) & cd .\$(TOIS) & md $(AUTHORS) $(AUTHORS)\src
	-robocopy .. .\$(TURNINDIR)\$(TOIS)\$(AUTHORS) odevzdani.txt /ZB /Z
	-robocopy .. .\$(TURNINDIR)\$(TOIS)\$(AUTHORS) hodnoceni.txt /ZB /Z
	-robocopy .. .\$(TURNINDIR)\$(TOIS)\$(AUTHORS) dokumentace.pdf /ZB /Z
	-robocopy . .\$(TURNINDIR)\$(TOIS)\$(AUTHORS)\src /E /ZB /Z /XD $(TOEXCLUDE)

docu: doc
	-robocopy .\html .\$(TURNINDIR)\$(TOSERVER)\$(AUTHORS)\$(DOCDIR) /E /ZB /Z
	del .\html /f /s /q & rmdir /s /q .\html
instal:
	if exist ".\$(PYINSTOK)" del .\$(PYINSTOK) /f /s /q & rmdir /s /q .\$(PYINSTOK)
	-pyinstaller -w --icon=$(PYASSETS)\logo.ico $(PROJECT).py
	del .\$(PYINSTIGNORE) /f /s /q & rmdir /s /q .\$(PYINSTIGNORE)
	cd .\$(WHEREEXE) & md $(PYASSETS)
	-robocopy .\$(PYASSETS) .\$(WHEREEXE)\$(PYASSETS) /E /ZB /Z
	-cd .\$(WHEREINSTALLSCRIPT) & iscc .\$(INSTALLERSCRIPT)
	-move /Y .\$(WHEREINSTALLER)\* .\$(TURNINDIR)\$(TOSERVER)\$(AUTHORS)\$(INSTALLDIR)
	del .\$(PYINSTOK) /f /s /q & rmdir /s /q .\$(PYINSTOK)
	del .\$(WHEREINSTALLER) /f /s /q & rmdir /s /q .\$(WHEREINSTALLER)

#Gets rid of __pycache__ and other stuff that is not going to be submitted
clean:
	cd .. & for /d /r . %%d in ("__pycache__") DO (if exist "%%d" del /f /s /q "%%d" & rmdir /s /q "%%d")
	cd .. & for /d /r . %%d in ("turnin") DO (if exist "%%d" del /f /s /q "%%d" & rmdir /s /q "%%d")
	del *.spec

#Executes tests
test:
	py -3 -m unittest tests.TestBaseOperations tests.TestAdvancedOperations

#Generates documentation
doc:
	-doxygen .\Doxyfile

#Executes calculator.py
run:
	py -3 $(PROJECT).py

profile:
	@echo Python program is not supposed to be built!
