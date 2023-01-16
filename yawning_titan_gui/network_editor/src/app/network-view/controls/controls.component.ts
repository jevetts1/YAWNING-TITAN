import { HttpClient } from '@angular/common/http';
import { Component, Inject } from '@angular/core';
import { DJANGO_SAVE_URL } from 'src/app/app.tokens';
import { CytoscapeService } from '../../services/cytoscape/cytoscape.service';

@Component({
  selector: 'app-controls',
  templateUrl: './controls.component.html',
  styleUrls: ['./controls.component.scss']
})
export class ControlsComponent {

  constructor(
    private cytoscapeService: CytoscapeService,
    private http: HttpClient,
    @Inject(DJANGO_SAVE_URL) private saveUrl
  ) { }

  /**
   * Returns a list of node ids
   * TODO: needs to return the full object
   * @returns
   */
  nodeList(): string[] {
    return this.cytoscapeService?.cytoscapeObj?.nodes().map(node => node.id())
  }

  /**
   * TODO: should download a json file containing the network
   */
  downloadNetwork(): void {
    console.log(this.cytoscapeService.getNetworkJson())
  }

  /**
   * Sends a post request to the django backend to save the file
   */
  saveNetwork(): void {
    this.http.post(
      this.saveUrl,
      this.cytoscapeService.getNetworkJson()
    ).subscribe()
  }

  resetView() {
    this.cytoscapeService.resetView();
  }
}
