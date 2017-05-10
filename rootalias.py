from ROOT import TH1D, TH2D, TCanvas, gPad, TLegend, gStyle, TGraph, kBlack, kRed, kBlue, kGreen

def set_legend_style(lg):
  lg.SetTextFont(43)
  lg.SetTextSize(28)
  lg.SetFillStyle(0)
  lg.SetMargin(0.4)
  lg.SetBorderSize(0)

def set_graph_style(gr):
  gr.SetMarkerStyle(24)
  gr.SetMarkerSize(1.2)
  gr.SetMarkerColor(kBlack)
  gr.GetYaxis().SetTitleOffset(1.2)
  gr.GetXaxis().SetTitleOffset(1.2)
  gr.GetXaxis().CenterTitle()
  gr.GetYaxis().CenterTitle()
  gr.GetXaxis().SetTitleFont(43)
  gr.GetYaxis().SetTitleFont(43)
  gr.GetXaxis().SetLabelFont(43)
  gr.GetYaxis().SetLabelFont(43)
  gr.GetXaxis().SetLabelSize(28)
  gr.GetYaxis().SetLabelSize(28)
  gr.GetXaxis().SetTitleSize(28)
  gr.GetYaxis().SetTitleSize(28)
  gr.SetLineWidth(2)
  gr.SetTitle("")

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
  h1.SetTitle("")

def set_margin():
  gPad.SetLeftMargin(0.15)
  gPad.SetBottomMargin(0.15)
