import math
from tkinter.font import Font
from tokenize import String

import classes
from api import *
from pygame import Color

from src import GraphAlgo
from src import GeoLocation
from src import DiGraph
from src import Node_data
from tkinter import filedialog, ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename


class Toolkit:
    pass


def repaint():
    pass


def revalidate():
    pass


class JPanel:
    pass


class GraphPanel(JPanel):

    # J
    def __init__(self, graphClass):
        # instance fields found by Java to Python Converter:
        self.graphClass: DiGraph
        self.a: GraphAlgo
        self.__minX = 0
        self.__minY = 0
        self.__maxX = 0
        self.__maxY = 0
        self.__UX = 0
        self.__UY = 0
        self.__screenSize = None

        self.__screenSize = Toolkit.getDefaultToolkit().getScreenSize()

        self.setPreferredSize(self.__screenSize)
        self.setBackground(Color(0x9FADBA))
        self.setFocusable(True)
        self.graphClass = graphClass
        (classes.AlgoGraphClass()).init(graphClass)
        print("start")
        self.__setLimits()

        self.__UX = self.__screenSize.getWidth() / abs(self.__maxX - self.__minX) * 0.90
        self.__UY = self.__screenSize.getHeight() / abs(self.__maxY - self.__minY) * 0.8

    def __setLimits(self):
        n = self.graphClass.nodeIter()
        node = None
        if n.hasNext():
            node = n.next()
            self.__minX = node.getLocation().x()
            self.__minY = node.getLocation().y()
            self.__maxX = node.getLocation().x()
            self.__maxY = node.getLocation().y()
        while n.hasNext():
            node = n.next()
            self.__minX = min(self.__minX, node.getLocation().x())
            self.__minY = min(self.__minY, node.getLocation().y())
            self.__maxX = max(self.__maxX, node.getLocation().x())
            self.__maxY = max(self.__maxY, node.getLocation().y())

    def paintComponent(self, g):
        super().paintComponent(g)
        self.draw(g)

    def draw(self, g):
        g.setFont(Font("david", Font.BOLD, 14))
        g.drawString(" Ofek Saadon ", 1000, 600)
        g.drawString(String.valueOf("MC: " + self.graphClass.getMC()), 1200, 25)
        iter2 = self.graphClass.edgeIter()
        while iter2.hasNext():
            edge = iter2.next()

            srcX = self.graphClass.getNode(edge.getSrc()).getLocation().x()
            srcX = ((srcX - self.__minX) * self.__UX) + 12
            srcY = self.graphClass.getNode(edge.getSrc()).getLocation().y()
            srcY = ((srcY - self.__minY) * self.__UY) + 12

            destX = self.graphClass.getNode(edge.getDest()).getLocation().x()
            destX = ((destX - self.__minX) * self.__UX) + 12
            destY = self.graphClass.getNode(edge.getDest()).getLocation().y()
            destY = ((destY - self.__minY) * self.__UY) + 12

            g.setColor(Color.GRAY)
            g.drawLine(int(srcX), int(srcY), int(destX), int(destY))
            self.__drawArrowLine(g, int(srcX), int(srcY), int(destX), int(destY), 30, 7)

        iter = self.graphClass.nodeIter()
        while iter.hasNext():
            N = iter.next()
            # draw the node
            x = int(((N.getLocation().x() - self.__minX) * self.__UX))
            y = int(((N.getLocation().y() - self.__minY) * self.__UY))
            g.setColor(Color.PINK)
            g.fillOval(x, y, 24, 24)
            g.setColor(Color.WHITE)
            g.drawString("" + N.getKey(), x + 8, y + 15)

    def __drawArrowLine(self, g, x1, y1, x2, y2, d, h):
        dx = x2 - x1
        dy = y2 - y1
        D = math.sqrt(dx * dx + dy * dy)
        xm = D - d
        xn = xm
        ym = h
        yn = -h
        x = None
        sin = dy / D
        cos = dx / D

        x = xm * cos - ym * sin + x1
        ym = xm * sin + ym * cos + y1
        xm = x

        x = xn * cos - yn * sin + x1
        yn = xn * sin + yn * cos + y1
        xn = x

        xpoints = [x2, int(xm), int(xn)]
        ypoints = [y2, int(ym), int(yn)]

        g.drawLine(x1, y1, x2, y2)
        g.fillPolygon(xpoints, ypoints, 3)

    def addNode(self, key, x, y):
        newX = (x - 12) / self.__UX + self.__minX
        newY = (y - 12) / self.__UY + self.__minY
        print("x" + x + "y=" + y)
        self.graphClass.addNode(classes.Node(key, classes.GeoLocationClass(newX + "," + newY + ",0")))
        repaint()
        revalidate()
