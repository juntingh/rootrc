import ROOT
from ROOT import TH1D, TH2D, TH3D, TCanvas, gPad, TLegend, gStyle, TGraph2D, TGraph, TGraphErrors, kWhite, kBlack, kGray, kRed, kBlue, kGreen, kOrange, kMagenta, kViolet, kAzure, kCyan, kTeal, kYellow, kSpring, kPink, TColor, TPaveStats, TFile, TF1, TPad, TLatex, TLine, TArrow, gROOT, TChain, kTRUE, kFALSE, TGaxis, TDatabasePDG, TMarker, gDirectory, THStack, TEllipse, TBox, TTimeStamp, TDatime, TSpectrum, TList, TPolyMarker, TPolyMarker3D, TNtuple, TGeoManager, TRandom
import numpy as np


COLORS = [kBlack, kBlue, kRed + 1, kMagenta + 2, kGreen + 1, kOrange + 1, kYellow + 2, kPink, kViolet, kAzure + 4, kCyan + 1, kTeal - 7, kBlue - 5]


def set_rooplot_style(frame):
    frame.SetMarkerStyle(24)
    frame.SetMarkerSize(1.2)
    frame.SetMarkerColor(kBlack)
    frame.GetYaxis().SetTitleOffset(1.2)
    frame.GetXaxis().SetTitleOffset(1.2)
    frame.GetXaxis().CenterTitle()
    frame.GetYaxis().CenterTitle()
    frame.GetXaxis().SetTitleFont(43)
    frame.GetYaxis().SetTitleFont(43)
    frame.GetXaxis().SetLabelFont(43)
    frame.GetYaxis().SetLabelFont(43)
    frame.GetXaxis().SetLabelSize(28)
    frame.GetYaxis().SetLabelSize(28)
    frame.GetXaxis().SetTitleSize(28)
    frame.GetYaxis().SetTitleSize(28)
    frame.SetTitle('')


def set_legend_style(lg):
    # lg.SetNColumns(2)
    lg.SetTextFont(43)
    lg.SetTextSize(28)
    lg.SetFillStyle(0)
    lg.SetMargin(0.4)
    lg.SetBorderSize(0)
    # lg1.SetFillStyle(1001) # solid


def set_graph_style(gr):
    gr.SetMarkerStyle(24)
    gr.SetMarkerSize(1.2)
    gr.SetMarkerColor(kBlack)

    axiss = [gr.GetXaxis(), gr.GetYaxis()]
    if type(gr) == TGraph2D:
        axiss = [gr.GetXaxis(), gr.GetYaxis(), gr.GetZaxis()]

    for axis in axiss:
        axis.SetTitleOffset(1.2)
        axis.CenterTitle()
        axis.SetTitleFont(43)
        axis.SetLabelFont(43)
        axis.SetLabelSize(28)
        axis.SetTitleSize(28)
    # gr.GetYaxis().SetDecimals() # same label width
    # gr.GetYaxis().SetMaxDigits(3) # changes power of 10
    gr.SetLineWidth(2)
    gr.SetTitle('')


def set_h1_style(h1):
    h1.GetYaxis().SetTitleOffset(1.3)
    h1.GetXaxis().SetTitleOffset(1.2)
    h1.GetXaxis().CenterTitle()
    h1.GetYaxis().CenterTitle()
    h1.GetXaxis().SetTitleFont(43)
    h1.GetYaxis().SetTitleFont(43)
    h1.GetXaxis().SetLabelFont(43)
    h1.GetYaxis().SetLabelFont(43)
    h1.GetXaxis().SetLabelSize(28)
    h1.GetYaxis().SetLabelSize(28)
    h1.GetXaxis().SetTitleSize(28)
    h1.GetYaxis().SetTitleSize(28)
    h1.GetYaxis().SetNdivisions(505, 1)
    h1.GetXaxis().SetNdivisions(505, 1)
    h1.SetLineWidth(2)
    h1.SetTitle('')


def set_h2_style(h2):
    gPad.SetRightMargin(0.2)
    h2.GetYaxis().SetTitleOffset(1.1)
    h2.GetXaxis().SetTitleOffset(1.05)
    h2.GetZaxis().SetTitleOffset(1.2)
    h2.GetXaxis().CenterTitle()
    h2.GetYaxis().CenterTitle()
    h2.GetZaxis().CenterTitle()
    h2.GetXaxis().SetTitleFont(43)
    h2.GetYaxis().SetTitleFont(43)
    h2.GetZaxis().SetTitleFont(43)
    h2.GetXaxis().SetLabelFont(43)
    h2.GetYaxis().SetLabelFont(43)
    h2.GetZaxis().SetLabelFont(43)
    h2.GetXaxis().SetLabelSize(28)
    h2.GetYaxis().SetLabelSize(28)
    h2.GetZaxis().SetLabelSize(28)
    h2.GetXaxis().SetTitleSize(28)
    h2.GetYaxis().SetTitleSize(28)
    h2.GetZaxis().SetTitleSize(28)
    h2.GetYaxis().SetNdivisions(505, 1)
    h2.GetXaxis().SetNdivisions(505, 1)
    h2.GetZaxis().SetNdivisions(505, 1)
    h2.SetTitle('')


def set_h2_color_style():
    n_rgb = 5
    n_contour = 255
    stops = np.array([0.00, 0.34, 0.61, 0.84, 1.00])
    reds = np.array([0.00, 0.00, 0.87, 1.00, 0.51])
    greens = np.array([0.00, 0.81, 1.00, 0.20, 0.00])
    blues = np.array([0.51, 1.00, 0.12, 0.00, 0.00])
    TColor.CreateGradientColorTable(n_rgb, stops, reds, greens, blues, n_contour)
    gStyle.SetNumberContours(n_contour)
    gPad.SetRightMargin(0.2)


def set_margin():
    gPad.SetLeftMargin(0.15)
    gPad.SetBottomMargin(0.15)


def get_max_y(h1s):
    max_y = 0.0
    for h1 in h1s:
        h1_maximum = h1.GetMaximum()
        if h1_maximum > max_y:
            max_y = h1_maximum
    return max_y


def draw_statbox(h1, **kwargs):
    # use c1.Update() beforehand
    x1 = kwargs.get('x1', 0.72)
    x2 = kwargs.get('x2', 0.98)
    y1 = kwargs.get('y1', 0.75)
    y2 = kwargs.get('y2', 0.935)

    p1 = h1.GetListOfFunctions().FindObject('stats')
    p1.SetX1NDC(x1)
    p1.SetY1NDC(y1)
    p1.SetX2NDC(x2)
    p1.SetY2NDC(y2)
    p1.Draw()


# def draw_statboxes(h1, h2, **kwargs):
#     position = kwargs.get('position', 'right')
#     if position not in ['left', 'right', 'top']:
#         raise Exception('The provided position option {} does not exist.'.format(position))

#     width = 0.23
#     height = 0.2
#     corner_x = 0.63
#     corner_y = 0.42
#     gap_y = 0.04
#     gap_x = 0.04
#     if position == 'left':
#         corner_x = 0.2
#     elif position == 'top':
#         corner_x = 0.19
#         corner_y = 0.66

#     ndcs_1 = [
#         corner_x,
#         corner_y,
#         corner_x + width,
#         corner_y + height
#     ]
#     ndcs_2 = [
#         corner_x,
#         corner_y + height + gap_y,
#         corner_x + width,
#         corner_y + height + gap_y + height
#     ]
#     if position == 'top':
#         ndcs_2 = [
#             corner_x + width + gap_x,
#             corner_y,
#             corner_x + width + gap_x + width,
#             corner_y + height
#         ]

#     p1 = h1.GetListOfFunctions().FindObject("stats")
#     p1.SetTextColor(h1.GetLineColor())
#     p1.SetLineColor(h1.GetLineColor())
#     p1.SetX1NDC(ndcs_1[0])
#     p1.SetY1NDC(ndcs_1[1])
#     p1.SetX2NDC(ndcs_1[2])
#     p1.SetY2NDC(ndcs_1[3])
#     p1.Draw()

#     p2 = h2.GetListOfFunctions().FindObject("stats")
#     p2.SetTextColor(h2.GetLineColor())
#     p2.SetLineColor(h2.GetLineColor())
#     p2.SetX1NDC(ndcs_2[0])
#     p2.SetY1NDC(ndcs_2[1])
#     p2.SetX2NDC(ndcs_2[2])
#     p2.SetY2NDC(ndcs_2[3])
#     p2.Draw()


def draw_statboxes(hs, **kwargs):
    width = kwargs.get('width', 0.23)
    height = kwargs.get('height', 0.2)
    corner_x = kwargs.get('corner_x', 0.72)
    corner_y = kwargs.get('corner_y', 0.27)
    gap_y = kwargs.get('gap_y', 0.04)
    delta_y = height + gap_y

    for i, h in enumerate(hs):
        p = h.GetListOfFunctions().FindObject("stats")
        p.SetTextColor(h.GetLineColor())
        p.SetLineColor(h.GetLineColor())
        p.SetX1NDC(corner_x)
        p.SetY1NDC(corner_y + delta_y * i)
        p.SetX2NDC(corner_x + width)
        p.SetY2NDC(corner_y + height + delta_y * i)
        p.Draw()


# def draw_statboxesss(h1, h2, h3, h4):
#     width = 0.18
#     height = 0.15
#     corner_x = 0.76
#     corner_y = 0.24
#     gap_y = 0.04
#     delta_y = height + gap_y

#     hs = [h1, h2, h3, h4]
#     for i, h in enumerate(hs):
#         p = h.GetListOfFunctions().FindObject("stats")
#         p.SetTextColor(h.GetLineColor())
#         p.SetLineColor(h.GetLineColor())
#         p.SetX1NDC(corner_x)
#         p.SetY1NDC(corner_y + delta_y * i)
#         p.SetX2NDC(corner_x + width)
#         p.SetY2NDC(corner_y + height + delta_y * i)
#         p.Draw()


def get_graph_from_hist(h1):
    xs = []
    ys = []
    x_errs = []
    y_errs = []

    for i in range(1, h1.GetNbinsX() + 1):
        xs.append(h1.GetBinCenter(i))
        ys.append(h1.GetBinContent(i))
        x_errs.append(h1.GetBinWidth(i) / 2.)
        y_errs.append((h1.GetBinContent(i))**0.5)

    return TGraphErrors(len(xs), np.array(xs), np.array(ys), np.array(x_errs), np.array(y_errs))


def get_graph_shade(gr1, gr2):
    xs = list(gr1.GetX())
    ys = list(gr1.GetY())
    xs.extend(reversed(list(gr2.GetX())))
    ys.extend(reversed(list(gr2.GetY())))
    return TGraph(len(xs), np.array(xs), np.array(ys))


def set_time_display(gr):
    gr.GetXaxis().SetTimeFormat('#splitline{%m/%d}{%Y} %F 1970-01-01 00:00:00')
    gr.GetXaxis().SetTimeDisplay(1)
    gr.GetYaxis().SetTitleOffset(1.5)
    gr.GetXaxis().SetLabelOffset(0.05)


def get_residual(h1, f1, x_min, x_max):
    xs = []
    diffs = []
    for i in range(h1.FindBin(x_min), h1.FindBin(x_max) + 1):
        diffs.append(h1.GetBinContent(i) - f1.Eval(h1.GetBinCenter(i)))
        xs.append(h1.GetBinCenter(i))
    return TGraph(len(xs), np.array(xs), np.array(diffs))


# gPad.Update()
# tl = TLine(gPad.GetUxmin(), gPad.GetUymin(), gPad.GetUxmax(), gPad.GetUymax())

# datetime.timestamp(datetime.strptime('2018/05/25', '%Y/%m/%d'))
# date.strftime('%Y/%m/%d')

# keys = [key.GetName() for key in tf.GetListOfKeys()]
# for key in tf.GetListOfKeys():
#     names.append(key.GetName())
