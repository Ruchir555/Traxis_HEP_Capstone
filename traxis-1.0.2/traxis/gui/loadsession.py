def loadJSON(self):

    # open file dialog for selecting a file to load from
    fileName = QtWidgets.QFileDialog.getOpenFileName(
        None, "Load Session", QtCore.QDir.currentPath(),
        "HEP Track Analysis (*.json);;All Files (*)")[0]

    fileName = self.cd(self,)

    # return if no file was selected
    if not fileName:
        return

    else:
        # open the file contents
        with open(fileName, 'r') as loadFile:
            # try to load the file contents as a JSON formatted object
            try:
                loadData = json.load(loadFile)
            except:
                self.displayMessage("NOTICE: Invalid JSON file: {}".format(
                    fileName))
                return

            # get the image filename from the saved session data
            imageFileName = loadData.get('imageFileName')

            # if the image filename is missing, return
            if not imageFileName:
                self.displayMessage("NOTICE: No image file name found in saved session data: {}".format(fileName))
                return

            # try to open the image. If it fails to open, return
            opened = self.openImage(imageFileName)
            if not opened:
                return

            # get the track marker data from the saved session
            points = loadData.get('points')
            if points:
                # add each track marker to the marker list
                for point in points:
                    pointDesignation = point["designation"]
                    x = point['x']
                    y = point['y']
                    addedMarker = self.markerList.addMarker(
                        x, y, self.pointSize,
                        self.lineWidth, self.scene)
                    # set the appropriate designation for each marker
                    addedMarker.setDesignation(pointDesignation)

            # get the dl data from the saved session
            dl = loadData.get('dl')
            # if it is a float, set it to the dl text box value
            try:
                float(dl)
                self.dlLineEdit.setText(dl)
            except (ValueError, TypeError):
                pass

            # get the data for the initial and final points for the
            # reference line
            refInitialPoint = loadData.get('refInitialPoint')
            refFinalPoint = loadData.get('refFinalPoint')
            if refInitialPoint and refFinalPoint:
                # set the initial point, line and final point of the
                # reference line
                self.angleRefLine.setInitialPoint(
                    refInitialPoint['x'], refInitialPoint['y'],
                    self.pointSize, self.lineWidth, self.scene)
                self.angleRefLine.drawLine(
                    refFinalPoint['x'], refFinalPoint['y'],
                    self.lineWidth, self.scene)
                self.angleRefLine.setFinalPoint(
                    refFinalPoint['x'], refFinalPoint['y'],
                    self.pointSize, self.lineWidth, self.scene)